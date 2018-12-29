# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 0.2; 25 0.2; 28 0.1; 31 0.1; 34 0.1; 37 -0.0; 41 -0.1; 45 -0.1; 49 -0.2; 54 -0.4; 60 -0.6; 66 -0.9; 72 -1.2; 79 -1.5; 87 -1.9; 96 -2.3; 106 -2.6; 116 -2.9; 128 -3.2; 141 -3.4; 155 -3.5; 170 -3.7; 187 -3.8; 206 -3.8; 227 -3.8; 249 -3.8; 274 -3.7; 302 -3.5; 332 -3.3; 365 -3.1; 402 -2.9; 442 -2.6; 486 -2.4; 535 -2.1; 588 -1.7; 647 -1.3; 712 -0.8; 783 -0.4; 861 -0.1; 947 0.0; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.1; 1526 0.4; 1678 1.1; 1846 1.7; 2031 2.0; 2234 1.8; 2457 0.8; 2703 -0.6; 2973 -1.7; 3270 -0.5; 3597 1.3; 3957 1.9; 4353 2.2; 4788 3.2; 5267 4.4; 5793 5.1; 6373 5.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.5; 15026 -1.8; 16529 -0.9; 18182 -1.6; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 220 Hz   | 0.52 | -4.0 dB  |
| Peaking | 2227 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2907 Hz  | 4.61 | -3.5 dB  |
| Peaking | 5719 Hz  | 2.42 | 5.5 dB   |
| Peaking | 20112 Hz | 2.21 | -10.8 dB |
| Peaking | 886 Hz   | 3.84 | 0.7 dB   |
| Peaking | 1326 Hz  | 4.76 | -0.6 dB  |
| Peaking | 6630 Hz  | 8.05 | 2.1 dB   |
| Peaking | 7700 Hz  | 2.63 | -1.4 dB  |
| Peaking | 17679 Hz | 7    | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)