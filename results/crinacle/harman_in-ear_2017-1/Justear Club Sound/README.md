# Justear Club Sound
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.3; 34 -4.7; 37 -5.0; 41 -5.4; 45 -5.7; 49 -6.1; 54 -6.6; 60 -7.1; 66 -7.7; 72 -8.2; 79 -8.8; 87 -9.4; 96 -10.2; 106 -10.8; 116 -11.2; 128 -11.7; 141 -12.0; 155 -12.0; 170 -11.9; 187 -11.7; 206 -11.3; 227 -10.8; 249 -10.3; 274 -9.8; 302 -9.1; 332 -8.5; 365 -7.9; 402 -7.5; 442 -7.1; 486 -6.7; 535 -6.4; 588 -6.2; 647 -5.9; 712 -5.4; 783 -5.0; 861 -4.7; 947 -4.8; 1042 -5.3; 1146 -6.2; 1261 -7.2; 1387 -7.7; 1526 -7.8; 1678 -7.7; 1846 -7.8; 2031 -8.0; 2234 -8.3; 2457 -8.5; 2703 -7.3; 2973 -4.8; 3270 -2.4; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -2.3; 5267 -6.7; 5793 -6.3; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.2; 15026 -17.7; 16529 -10.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Justear Club Sound GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Justear Club Sound ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.72 | 3.8 dB   |
| Peaking | 150 Hz   | 0.84 | -6.0 dB  |
| Peaking | 4024 Hz  | 2.82 | 7.0 dB   |
| Peaking | 15244 Hz | 3.56 | -12.7 dB |
| Peaking | 20797 Hz | 1.42 | 2.0 dB   |
| Peaking | 857 Hz   | 1.76 | 2.6 dB   |
| Peaking | 2526 Hz  | 0.87 | -3.2 dB  |
| Peaking | 3267 Hz  | 3.28 | 4.0 dB   |
| Peaking | 6633 Hz  | 7.96 | 5.2 dB   |
| Peaking | 20109 Hz | 2.26 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Justear%20Club%20Sound/Justear%20Club%20Sound.png)