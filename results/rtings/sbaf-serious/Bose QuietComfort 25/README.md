# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.6; 23 -2.5; 25 -2.4; 28 -2.3; 31 -2.2; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.4; 66 -3.5; 72 -3.4; 79 -3.3; 87 -3.2; 96 -3.3; 106 -3.4; 116 -3.6; 128 -3.7; 141 -3.8; 155 -3.7; 170 -3.6; 187 -3.5; 206 -3.2; 227 -2.9; 249 -2.6; 274 -2.3; 302 -2.0; 332 -1.7; 365 -1.3; 402 -1.2; 442 -1.1; 486 -0.8; 535 -0.6; 588 -0.4; 647 -0.2; 712 0.2; 783 0.0; 861 -0.0; 947 0.0; 1042 -0.1; 1146 -0.8; 1261 -2.5; 1387 -4.2; 1526 -4.8; 1678 -6.0; 1846 -6.5; 2031 -6.1; 2234 -5.1; 2457 -3.3; 2703 -0.9; 2973 1.0; 3270 -0.4; 3597 -2.6; 3957 -2.7; 4353 -0.7; 4788 4.2; 5267 6.0; 5793 1.9; 6373 -5.2; 7010 0.6; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.37 | -3.0 dB |
| Peaking | 179 Hz  | 0.93 | -2.4 dB |
| Peaking | 1844 Hz | 2.03 | -7.0 dB |
| Peaking | 5270 Hz | 5.74 | 7.8 dB  |
| Peaking | 6336 Hz | 9.29 | -6.8 dB |
| Peaking | 1051 Hz | 1.7  | 1.3 dB  |
| Peaking | 1372 Hz | 3.88 | -2.3 dB |
| Peaking | 2386 Hz | 2.88 | -4.0 dB |
| Peaking | 3041 Hz | 1.35 | 5.6 dB  |
| Peaking | 3710 Hz | 3.12 | -6.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)