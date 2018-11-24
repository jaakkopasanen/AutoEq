# Audio Technical ATH-ES55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.8; 141 5.2; 155 4.8; 170 4.4; 187 3.9; 206 3.6; 227 3.3; 249 3.2; 274 3.6; 302 3.8; 332 3.7; 365 3.2; 402 3.2; 442 3.6; 486 3.4; 535 3.4; 588 3.5; 647 2.9; 712 1.9; 783 1.3; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -2.1; 1678 -2.2; 1846 -2.0; 2031 -1.0; 2234 0.3; 2457 2.2; 2703 3.7; 2973 5.0; 3270 5.1; 3597 5.3; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -0.2; 18182 -0.7; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technical ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.11 | 6.0 dB  |
| Peaking | 119 Hz  | 0.78 | 2.7 dB  |
| Peaking | 468 Hz  | 0.94 | 3.1 dB  |
| Peaking | 1661 Hz | 1.53 | -4.1 dB |
| Peaking | 4096 Hz | 0.98 | 7.0 dB  |
| Peaking | 394 Hz  | 8.52 | -0.5 dB |
| Peaking | 2893 Hz | 3.18 | 2.3 dB  |
| Peaking | 3357 Hz | 1.34 | -1.4 dB |
| Peaking | 6255 Hz | 2.61 | 5.0 dB  |
| Peaking | 7379 Hz | 1.47 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-ES55/Audio%20Technical%20ATH-ES55.png)