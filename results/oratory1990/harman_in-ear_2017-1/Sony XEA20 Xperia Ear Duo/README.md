# Sony XEA20 Xperia Ear Duo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.1; 170 -2.1; 187 -3.3; 206 -4.6; 227 -5.2; 249 -6.0; 274 -7.1; 302 -7.6; 332 -7.8; 365 -8.2; 402 -8.6; 442 -8.8; 486 -9.0; 535 -9.1; 588 -9.3; 647 -9.5; 712 -9.7; 783 -10.1; 861 -10.6; 947 -11.2; 1042 -12.8; 1146 -14.3; 1261 -14.9; 1387 -12.5; 1526 -8.7; 1678 -5.8; 1846 -4.4; 2031 -4.4; 2234 -5.7; 2457 -7.5; 2703 -9.8; 2973 -9.5; 3270 -7.3; 3597 -6.3; 3957 -7.1; 4353 -8.5; 4788 -9.7; 5267 -8.7; 5793 -6.7; 6373 -5.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.5; 13660 -17.4; 15026 -26.1; 16529 -23.1; 18182 -7.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XEA20 Xperia Ear Duo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XEA20 Xperia Ear Duo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.36 | 6.9 dB   |
| Peaking | 1004 Hz  | 1.16 | -6.6 dB  |
| Peaking | 4786 Hz  | 7.1  | -2.9 dB  |
| Peaking | 15633 Hz | 2.54 | -22.9 dB |
| Peaking | 22050 Hz | 1.12 | -15.5 dB |
| Peaking | 1424 Hz  | 0.2  | -1.1 dB  |
| Peaking | 1888 Hz  | 3.82 | 5.9 dB   |
| Peaking | 6803 Hz  | 5.17 | 4.0 dB   |
| Peaking | 11897 Hz | 1.64 | 4.8 dB   |
| Peaking | 14149 Hz | 3.13 | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 6.1 dB   |
| Peaking | 250 Hz   | 1.41 | -0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XEA20%20Xperia%20Ear%20Duo/Sony%20XEA20%20Xperia%20Ear%20Duo.png)