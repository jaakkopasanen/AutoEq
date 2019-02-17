# Sony XEA20 Xperia Ear Duo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.6; 274 -1.6; 302 -2.1; 332 -2.3; 365 -2.7; 402 -3.1; 442 -3.3; 486 -3.6; 535 -3.6; 588 -3.8; 647 -4.0; 712 -4.2; 783 -4.6; 861 -5.1; 947 -5.7; 1042 -7.3; 1146 -8.7; 1261 -9.5; 1387 -7.0; 1526 -3.2; 1678 -0.6; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -2.0; 2703 -4.3; 2973 -4.0; 3270 -1.8; 3597 -0.8; 3957 -1.6; 4353 -3.0; 4788 -4.2; 5267 -3.2; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.9; 15026 -20.5; 16529 -17.6; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XEA20 Xperia Ear Duo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XEA20 Xperia Ear Duo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 66 Hz    | 0.16 | 6.4 dB   |
| Peaking | 1981 Hz  | 3.31 | 5.7 dB   |
| Peaking | 4784 Hz  | 0.88 | 4.6 dB   |
| Peaking | 12575 Hz | 3.65 | 4.3 dB   |
| Peaking | 15383 Hz | 2.01 | -16.6 dB |
| Peaking | 1242 Hz  | 2.72 | -5.7 dB  |
| Peaking | 1618 Hz  | 7.23 | 3.5 dB   |
| Peaking | 2450 Hz  | 0.16 | 1.0 dB   |
| Peaking | 6169 Hz  | 1.56 | -5.7 dB  |
| Peaking | 6229 Hz  | 3.84 | 7.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.8 dB   |
| Peaking | 250 Hz   | 1.41 | 4.4 dB   |
| Peaking | 500 Hz   | 1.41 | 2.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -12.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XEA20%20Xperia%20Ear%20Duo/Sony%20XEA20%20Xperia%20Ear%20Duo.png)