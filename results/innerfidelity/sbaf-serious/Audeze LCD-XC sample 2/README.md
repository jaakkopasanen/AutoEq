# Audeze LCD-XC sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 4.0; 66 2.8; 72 2.6; 79 2.4; 87 2.1; 96 1.9; 106 1.9; 116 1.8; 128 1.6; 141 1.6; 155 1.8; 170 1.5; 187 1.4; 206 1.6; 227 1.9; 249 2.1; 274 2.3; 302 2.4; 332 2.5; 365 2.5; 402 2.3; 442 2.3; 486 1.8; 535 1.8; 588 2.1; 647 2.1; 712 1.4; 783 1.1; 861 0.5; 947 0.2; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.7; 1526 -3.7; 1678 -4.3; 1846 -4.1; 2031 -3.0; 2234 -1.5; 2457 0.6; 2703 1.8; 2973 2.9; 3270 3.8; 3597 4.5; 3957 2.7; 4353 -1.5; 4788 -3.4; 5267 3.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.4; 16529 -0.6; 18182 -2.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.62 | 6.6 dB  |
| Peaking | 412 Hz  | 0.61 | 2.4 dB  |
| Peaking | 1677 Hz | 1.79 | -5.0 dB |
| Peaking | 3252 Hz | 3.32 | 5.0 dB  |
| Peaking | 6066 Hz | 5.33 | 6.8 dB  |
| Peaking | 53 Hz   | 5.52 | 1.0 dB  |
| Peaking | 2583 Hz | 9.59 | 1.5 dB  |
| Peaking | 3806 Hz | 7.53 | 3.0 dB  |
| Peaking | 4770 Hz | 4.15 | -6.0 dB |
| Peaking | 5385 Hz | 8.4  | 5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%202/Audeze%20LCD-XC%20sample%202.png)