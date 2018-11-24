# Sennheiser HD 598 Cs

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.2; 28 3.9; 31 3.6; 34 3.5; 37 3.5; 41 3.4; 45 3.3; 49 3.1; 54 2.9; 60 2.6; 66 2.4; 72 2.3; 79 2.2; 87 1.9; 96 1.6; 106 1.1; 116 0.7; 128 0.5; 141 0.6; 155 0.8; 170 1.1; 187 1.5; 206 2.2; 227 3.0; 249 3.8; 274 4.4; 302 4.6; 332 4.2; 365 3.5; 402 2.5; 442 1.6; 486 0.8; 535 0.8; 588 0.8; 647 0.9; 712 0.5; 783 0.2; 861 -0.0; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.2; 1526 -0.3; 1678 -0.3; 1846 -0.1; 2031 0.2; 2234 1.1; 2457 2.4; 2703 3.7; 2973 4.0; 3270 3.3; 3597 2.8; 3957 4.0; 4353 3.9; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 Cs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 Cs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.62 | 4.6 dB  |
| Peaking | 58 Hz   | 1.15 | 1.7 dB  |
| Peaking | 297 Hz  | 1.73 | 4.7 dB  |
| Peaking | 2905 Hz | 3.19 | 3.5 dB  |
| Peaking | 5343 Hz | 2.15 | 6.6 dB  |
| Peaking | 132 Hz  | 4.65 | -0.6 dB |
| Peaking | 1723 Hz | 4.27 | -0.9 dB |
| Peaking | 3949 Hz | 6.91 | 1.4 dB  |
| Peaking | 6489 Hz | 4.92 | 3.5 dB  |
| Peaking | 7394 Hz | 1.5  | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20598%20Cs/Sennheiser%20HD%20598%20Cs.png)