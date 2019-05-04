# BGVP DM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.4; 25 -2.8; 28 -3.2; 31 -3.6; 34 -3.9; 37 -4.1; 41 -4.5; 45 -4.8; 49 -5.1; 54 -5.4; 60 -5.7; 66 -6.1; 72 -6.5; 79 -6.9; 87 -7.4; 96 -7.8; 106 -8.2; 116 -8.6; 128 -8.9; 141 -9.1; 155 -9.3; 170 -9.5; 187 -9.6; 206 -9.7; 227 -9.7; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.3; 442 -7.9; 486 -7.4; 535 -6.7; 588 -6.1; 647 -5.5; 712 -4.9; 783 -4.4; 861 -4.1; 947 -4.3; 1042 -4.8; 1146 -5.4; 1261 -5.6; 1387 -5.6; 1526 -5.3; 1678 -5.0; 1846 -4.7; 2031 -4.0; 2234 -2.6; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.7; 3957 -5.4; 4353 -7.9; 4788 -6.9; 5267 -6.7; 5793 -9.0; 6373 -11.6; 7010 -11.0; 7711 -10.9; 8482 -9.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.5; 16529 -12.4; 18182 -11.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.59 | 4.5 dB  |
| Peaking | 191 Hz   | 0.81 | -3.6 dB |
| Peaking | 2824 Hz  | 1.54 | 6.8 dB  |
| Peaking | 6719 Hz  | 2.18 | -5.8 dB |
| Peaking | 17265 Hz | 2.06 | -7.1 dB |
| Peaking | 370 Hz   | 2.26 | -0.9 dB |
| Peaking | 816 Hz   | 2.22 | 2.6 dB  |
| Peaking | 3479 Hz  | 8.52 | 1.9 dB  |
| Peaking | 4252 Hz  | 7.23 | -3.0 dB |
| Peaking | 12111 Hz | 1.44 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/BGVP%20DM6/BGVP%20DM6.png)