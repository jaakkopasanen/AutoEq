# Ocharaku Co-Donguri Shizuku
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.6; 28 -7.9; 31 -8.1; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.3; 49 -8.4; 54 -8.5; 60 -8.7; 66 -8.8; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.7; 128 -9.7; 141 -9.9; 155 -9.8; 170 -9.6; 187 -9.4; 206 -9.1; 227 -8.8; 249 -8.4; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.2; 402 -5.7; 442 -5.3; 486 -4.8; 535 -4.3; 588 -3.9; 647 -3.4; 712 -3.0; 783 -2.6; 861 -2.4; 947 -2.4; 1042 -2.8; 1146 -3.5; 1261 -4.1; 1387 -4.4; 1526 -4.5; 1678 -4.9; 1846 -5.4; 2031 -5.6; 2234 -6.5; 2457 -9.3; 2703 -11.0; 2973 -9.4; 3270 -7.2; 3597 -6.6; 3957 -7.9; 4353 -11.2; 4788 -11.0; 5267 -5.1; 5793 -0.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.1; 13660 -12.8; 15026 -20.8; 16529 -25.8; 18182 -25.9; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Co-Donguri Shizuku GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Co-Donguri Shizuku ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 130 Hz   | 0.36 | -4.2 dB  |
| Peaking | 2695 Hz  | 0.77 | -15.4 dB |
| Peaking | 4565 Hz  | 5.44 | -9.8 dB  |
| Peaking | 6034 Hz  | 0.17 | 17.8 dB  |
| Peaking | 17116 Hz | 0.41 | -30.7 dB |
| Peaking | 2146 Hz  | 8.26 | 2.0 dB   |
| Peaking | 6206 Hz  | 3.75 | 5.8 dB   |
| Peaking | 7466 Hz  | 1.44 | -4.1 dB  |
| Peaking | 12413 Hz | 2.41 | 5.2 dB   |
| Peaking | 14874 Hz | 3.05 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Co-Donguri%20Shizuku/Ocharaku%20Co-Donguri%20Shizuku.png)