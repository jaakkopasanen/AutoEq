# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.1; 28 -4.1; 31 -4.2; 34 -4.2; 37 -4.1; 41 -4.0; 45 -3.9; 49 -3.7; 54 -3.3; 60 -3.1; 66 -3.4; 72 -4.2; 79 -4.8; 87 -5.1; 96 -5.4; 106 -5.5; 116 -5.5; 128 -5.6; 141 -5.5; 155 -5.1; 170 -4.1; 187 -3.7; 206 -2.2; 227 -0.0; 249 1.8; 274 2.2; 302 1.2; 332 0.4; 365 0.3; 402 0.2; 442 1.0; 486 0.4; 535 -0.1; 588 -0.1; 647 -0.0; 712 -0.2; 783 0.2; 861 0.1; 947 0.1; 1042 0.0; 1146 -0.2; 1261 -0.7; 1387 -1.6; 1526 -2.5; 1678 -3.0; 1846 -3.1; 2031 -2.3; 2234 -1.4; 2457 -1.7; 2703 -1.2; 2973 -0.1; 3270 1.6; 3597 3.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.4; 6373 1.2; 7010 2.5; 7711 0.3; 8482 -1.0; 9330 -5.0; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.4; 18182 -3.2; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.48 | -4.1 dB |
| Peaking | 121 Hz  | 1.52 | -5.3 dB |
| Peaking | 2030 Hz | 1.42 | -3.6 dB |
| Peaking | 4508 Hz | 1.68 | 7.2 dB  |
| Peaking | 9269 Hz | 6.3  | -6.2 dB |
| Peaking | 186 Hz  | 3    | -2.1 dB |
| Peaking | 260 Hz  | 3.14 | 3.7 dB  |
| Peaking | 446 Hz  | 6.01 | 1.0 dB  |
| Peaking | 1060 Hz | 1.79 | 0.7 dB  |
| Peaking | 1559 Hz | 4.63 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)