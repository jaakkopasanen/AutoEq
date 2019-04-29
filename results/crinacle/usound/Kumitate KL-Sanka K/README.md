# Kumitate KL-Sanka K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.2; 66 -8.5; 72 -8.7; 79 -9.0; 87 -9.3; 96 -9.7; 106 -9.9; 116 -10.1; 128 -10.2; 141 -10.3; 155 -10.3; 170 -10.2; 187 -9.9; 206 -9.5; 227 -9.0; 249 -8.4; 274 -7.9; 302 -7.3; 332 -6.6; 365 -6.0; 402 -5.5; 442 -4.9; 486 -4.5; 535 -4.0; 588 -3.5; 647 -3.0; 712 -2.4; 783 -1.9; 861 -1.4; 947 -1.2; 1042 -1.2; 1146 -1.6; 1261 -2.1; 1387 -2.2; 1526 -1.7; 1678 -0.9; 1846 -0.9; 2031 -2.5; 2234 -4.3; 2457 -4.5; 2703 -3.0; 2973 -1.6; 3270 -0.6; 3597 -0.5; 3957 -1.8; 4353 -4.5; 4788 -6.6; 5267 -6.0; 5793 -5.8; 6373 -9.0; 7010 -13.9; 7711 -14.4; 8482 -15.6; 9330 -15.9; 10263 -10.7; 11289 -5.9; 12418 -5.9; 13660 -7.9; 15026 -14.7; 16529 -11.6; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1193 Hz  | 0.92 | 4.9 dB   |
| Peaking | 3487 Hz  | 2.77 | 5.8 dB   |
| Peaking | 5785 Hz  | 7.18 | 2.6 dB   |
| Peaking | 8211 Hz  | 1.96 | -10.9 dB |
| Peaking | 15500 Hz | 3.54 | -10.1 dB |
| Peaking | 98 Hz    | 0.24 | -1.2 dB  |
| Peaking | 159 Hz   | 0.6  | -4.0 dB  |
| Peaking | 550 Hz   | 0.49 | 2.0 dB   |
| Peaking | 1239 Hz  | 4.04 | -2.2 dB  |
| Peaking | 11830 Hz | 4.55 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Sanka%20K/Kumitate%20KL-Sanka%20K.png)