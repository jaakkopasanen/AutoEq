# Sennheiser IE80 Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.8; 25 -10.1; 28 -10.6; 31 -10.9; 34 -11.2; 37 -11.4; 41 -11.7; 45 -11.9; 49 -12.0; 54 -12.2; 60 -12.4; 66 -12.6; 72 -12.9; 79 -13.1; 87 -13.3; 96 -13.5; 106 -13.7; 116 -13.7; 128 -13.7; 141 -13.7; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.8; 227 -12.4; 249 -11.9; 274 -11.5; 302 -10.9; 332 -10.3; 365 -9.7; 402 -9.2; 442 -8.8; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.2; 861 -5.8; 947 -5.5; 1042 -5.4; 1146 -5.6; 1261 -5.7; 1387 -5.4; 1526 -4.7; 1678 -3.8; 1846 -2.7; 2031 -1.6; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -2.2; 4353 -4.2; 4788 -7.6; 5267 -10.3; 5793 -6.2; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.4; 15026 -24.5; 16529 -26.1; 18182 -24.1; 20000 -19.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.33 | -5.2 dB  |
| Peaking | 184 Hz   | 0.66 | -3.9 dB  |
| Peaking | 2762 Hz  | 0.91 | 8.7 dB   |
| Peaking | 11734 Hz | 0.53 | 22.0 dB  |
| Peaking | 15899 Hz | 0.38 | -33.9 dB |
| Peaking | 871 Hz   | 4.01 | 0.9 dB   |
| Peaking | 3890 Hz  | 4.12 | 1.8 dB   |
| Peaking | 5275 Hz  | 4.47 | -6.1 dB  |
| Peaking | 6461 Hz  | 5.04 | 6.4 dB   |
| Peaking | 10278 Hz | 4.59 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -23.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80%20Half/Sennheiser%20IE80%20Half.png)