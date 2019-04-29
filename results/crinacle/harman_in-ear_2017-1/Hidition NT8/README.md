# Hidition NT8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.6; 28 -5.7; 31 -5.8; 34 -5.8; 37 -5.7; 41 -5.7; 45 -5.6; 49 -5.6; 54 -5.6; 60 -5.6; 66 -5.7; 72 -5.8; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.7; 116 -6.9; 128 -7.1; 141 -7.3; 155 -7.5; 170 -7.5; 187 -7.7; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.8; 365 -7.7; 402 -7.8; 442 -7.8; 486 -7.8; 535 -7.9; 588 -7.9; 647 -8.0; 712 -8.0; 783 -8.1; 861 -8.4; 947 -8.9; 1042 -9.7; 1146 -10.8; 1261 -11.6; 1387 -11.6; 1526 -10.9; 1678 -9.8; 1846 -8.5; 2031 -7.1; 2234 -5.5; 2457 -4.1; 2703 -3.1; 2973 -2.9; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.2; 7711 -8.8; 8482 -9.9; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.5; 15026 -23.2; 16529 -31.3; 18182 -29.4; 20000 -17.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 317 Hz   | 0.7  | -1.5 dB  |
| Peaking | 1429 Hz  | 1.07 | -9.2 dB  |
| Peaking | 8318 Hz  | 2.51 | -13.2 dB |
| Peaking | 8895 Hz  | 0.31 | 23.2 dB  |
| Peaking | 16906 Hz | 0.52 | -39.0 dB |
| Peaking | 20 Hz    | 0.84 | 1.2 dB   |
| Peaking | 60 Hz    | 1.73 | 0.9 dB   |
| Peaking | 9870 Hz  | 4.6  | -1.6 dB  |
| Peaking | 13173 Hz | 3.74 | 5.6 dB   |
| Peaking | 15359 Hz | 3.71 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hidition%20NT8/Hidition%20NT8.png)