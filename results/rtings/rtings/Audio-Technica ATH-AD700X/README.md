# Audio-Technica ATH-AD700X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.9; 72 4.4; 79 3.8; 87 3.3; 96 2.7; 106 2.0; 116 1.6; 128 1.1; 141 0.8; 155 0.6; 170 0.4; 187 0.2; 206 0.3; 227 0.4; 249 0.5; 274 0.6; 302 0.6; 332 0.4; 365 0.3; 402 0.2; 442 -0.0; 486 -0.1; 535 -0.1; 588 0.2; 647 0.3; 712 0.3; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.9; 1526 -1.0; 1678 -0.8; 1846 -0.2; 2031 0.8; 2234 3.3; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.0; 3957 0.7; 4353 2.0; 4788 6.0; 5267 6.0; 5793 4.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -5.8; 10263 -6.4; 11289 -1.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.55 | 6.7 dB  |
| Peaking | 1721 Hz | 1.78 | -2.6 dB |
| Peaking | 2729 Hz | 1.92 | 6.9 dB  |
| Peaking | 5686 Hz | 2.08 | 5.6 dB  |
| Peaking | 9818 Hz | 4.33 | -8.4 dB |
| Peaking | 31 Hz   | 0.16 | 1.8 dB  |
| Peaking | 34 Hz   | 1.34 | -2.5 dB |
| Peaking | 140 Hz  | 0.93 | -1.8 dB |
| Peaking | 4098 Hz | 7.57 | -7.4 dB |
| Peaking | 4156 Hz | 2.89 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)