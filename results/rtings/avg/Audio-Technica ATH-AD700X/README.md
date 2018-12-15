# Audio-Technica ATH-AD700X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.9; 72 4.4; 79 3.8; 87 3.3; 96 2.7; 106 2.0; 116 1.6; 128 1.1; 141 0.8; 155 0.6; 170 0.4; 187 0.2; 206 0.3; 227 0.4; 249 0.5; 274 0.6; 302 0.6; 332 0.4; 365 0.3; 402 0.2; 442 -0.0; 486 -0.1; 535 -0.1; 588 0.2; 647 0.3; 712 0.3; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.9; 1526 -1.0; 1678 -0.8; 1846 -0.2; 2031 0.8; 2234 3.3; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 4.0; 3957 -0.5; 4353 0.7; 4788 5.9; 5267 5.8; 5793 1.8; 6373 5.1; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -4.4; 10263 -4.7; 11289 -1.6; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.9; 18182 -3.6; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.55 | 6.7 dB  |
| Peaking | 1685 Hz | 1.89 | -2.3 dB |
| Peaking | 2723 Hz | 2.19 | 6.9 dB  |
| Peaking | 5818 Hz | 1.82 | 4.3 dB  |
| Peaking | 9807 Hz | 3.52 | -6.2 dB |
| Peaking | 67 Hz   | 2.67 | 0.7 dB  |
| Peaking | 158 Hz  | 2.1  | -0.7 dB |
| Peaking | 3485 Hz | 5.8  | 3.6 dB  |
| Peaking | 4129 Hz | 3.68 | -5.6 dB |
| Peaking | 4715 Hz | 6.66 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)