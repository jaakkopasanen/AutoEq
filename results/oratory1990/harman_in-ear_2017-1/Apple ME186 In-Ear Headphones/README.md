# Apple ME186 In-Ear Headphones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 5.1; 79 4.2; 87 3.3; 96 2.3; 106 1.4; 116 0.5; 128 -0.3; 141 -1.1; 155 -1.8; 170 -2.5; 187 -3.1; 206 -3.6; 227 -3.9; 249 -4.1; 274 -4.0; 302 -3.8; 332 -3.5; 365 -3.2; 402 -2.9; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.5; 647 -1.1; 712 -0.7; 783 -0.3; 861 0.0; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 0.0; 1387 0.5; 1526 1.3; 1678 2.0; 1846 2.7; 2031 3.3; 2234 3.7; 2457 3.4; 2703 2.3; 2973 1.4; 3270 2.6; 3597 4.1; 3957 4.3; 4353 4.2; 4788 4.9; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.8; 13660 -8.6; 15026 -17.3; 16529 -19.0; 18182 -17.3; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.31 | 7.8 dB   |
| Peaking | 201 Hz   | 0.52 | -7.0 dB  |
| Peaking | 801 Hz   | 2.92 | 0.8 dB   |
| Peaking | 2196 Hz  | 1.55 | 3.5 dB   |
| Peaking | 5305 Hz  | 2.26 | 6.4 dB   |
| Peaking | 7075 Hz  | 0.66 | 4.5 dB   |
| Peaking | 12131 Hz | 1.82 | 9.8 dB   |
| Peaking | 15384 Hz | 1.88 | -9.8 dB  |
| Peaking | 19720 Hz | 0.15 | -10.2 dB |
| Peaking | 20688 Hz | 0.59 | -10.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)