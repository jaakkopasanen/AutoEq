# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.4; 25 -8.5; 28 -8.6; 31 -8.7; 34 -8.7; 37 -8.8; 41 -8.8; 45 -8.9; 49 -9.0; 54 -9.1; 60 -9.3; 66 -9.4; 72 -9.6; 79 -9.8; 87 -9.9; 96 -10.1; 106 -10.2; 116 -10.3; 128 -10.3; 141 -10.2; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.4; 227 -9.1; 249 -8.9; 274 -8.5; 302 -8.1; 332 -7.7; 365 -7.4; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.5; 588 -6.3; 647 -6.1; 712 -6.1; 783 -6.0; 861 -6.3; 947 -6.8; 1042 -7.6; 1146 -8.3; 1261 -8.9; 1387 -9.3; 1526 -9.6; 1678 -9.8; 1846 -9.8; 2031 -9.1; 2234 -7.3; 2457 -4.6; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.8; 9330 -17.3; 10263 -19.3; 11289 -15.5; 12418 -10.6; 13660 -11.5; 15026 -17.4; 16529 -23.1; 18182 -27.2; 20000 -30.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.34 | -2.1 dB  |
| Peaking | 144 Hz   | 0.78 | -2.8 dB  |
| Peaking | 1735 Hz  | 1.74 | -6.0 dB  |
| Peaking | 4342 Hz  | 0.82 | 9.7 dB   |
| Peaking | 19637 Hz | 0.27 | -23.4 dB |
| Peaking | 753 Hz   | 1.51 | 1.0 dB   |
| Peaking | 1167 Hz  | 3.35 | -1.2 dB  |
| Peaking | 6809 Hz  | 2.68 | 4.0 dB   |
| Peaking | 9972 Hz  | 2.76 | -10.1 dB |
| Peaking | 13063 Hz | 2.5  | 8.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -24.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20KSE1500/Shure%20KSE1500.png)