# Shozy & Neo BG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.5; 28 -6.0; 31 -6.3; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.3; 49 -7.6; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.4; 96 -9.8; 106 -10.2; 116 -10.5; 128 -10.7; 141 -10.9; 155 -10.9; 170 -11.1; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.8; 274 -10.6; 302 -10.3; 332 -9.8; 365 -9.4; 402 -9.0; 442 -8.6; 486 -8.1; 535 -7.6; 588 -7.1; 647 -6.6; 712 -6.1; 783 -5.6; 861 -5.3; 947 -5.3; 1042 -5.7; 1146 -6.4; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.5; 1846 -8.8; 2031 -7.5; 2234 -4.2; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -1.8; 3597 -1.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -4.2; 6373 -6.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.3; 15026 -18.0; 16529 -25.4; 18182 -24.5; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo BG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo BG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 215 Hz   | 0.44 | -5.3 dB  |
| Peaking | 1872 Hz  | 1.31 | -10.8 dB |
| Peaking | 2512 Hz  | 1.32 | 7.3 dB   |
| Peaking | 4420 Hz  | 0.12 | 5.0 dB   |
| Peaking | 17383 Hz | 0.93 | -24.1 dB |
| Peaking | 20 Hz    | 1.56 | 2.2 dB   |
| Peaking | 4935 Hz  | 2.41 | 6.1 dB   |
| Peaking | 5790 Hz  | 1.34 | -5.0 dB  |
| Peaking | 12974 Hz | 2.41 | 4.9 dB   |
| Peaking | 15654 Hz | 3.3  | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20&%20Neo%20BG/Shozy%20&%20Neo%20BG.png)