# Beats Executive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.7; 45 -3.1; 49 -4.3; 54 -5.5; 60 -6.8; 66 -7.8; 72 -8.6; 79 -9.5; 87 -10.4; 96 -11.2; 106 -11.9; 116 -12.5; 128 -13.0; 141 -13.3; 155 -13.4; 170 -13.4; 187 -13.2; 206 -12.7; 227 -11.9; 249 -10.9; 274 -9.4; 302 -7.5; 332 -5.5; 365 -3.4; 402 -1.7; 442 -1.0; 486 -1.4; 535 -1.2; 588 -0.8; 647 -0.9; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -1.3; 1261 -1.7; 1387 -3.3; 1526 -4.4; 1678 -5.2; 1846 -6.8; 2031 -8.0; 2234 -8.8; 2457 -9.1; 2703 -9.0; 2973 -9.8; 3270 -12.8; 3597 -9.6; 3957 -4.0; 4353 -5.3; 4788 -8.9; 5267 -6.5; 5793 -4.5; 6373 -4.1; 7010 -5.3; 7711 -8.8; 8482 -9.1; 9330 -7.4; 10263 -7.7; 11289 -7.4; 12418 -6.5; 13660 -7.7; 15026 -11.4; 16529 -10.6; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.69 | 8.0 dB  |
| Peaking | 184 Hz   | 0.41 | -9.5 dB |
| Peaking | 420 Hz   | 1.11 | 9.4 dB  |
| Peaking | 934 Hz   | 0.98 | 6.5 dB  |
| Peaking | 2752 Hz  | 1.68 | -4.7 dB |
| Peaking | 6169 Hz  | 3.64 | 2.1 dB  |
| Peaking | 6820 Hz  | 3.75 | 2.8 dB  |
| Peaking | 7450 Hz  | 2.13 | -0.6 dB |
| Peaking | 7957 Hz  | 3.6  | -3.5 dB |
| Peaking | 15697 Hz | 2.51 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | 6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Executive/Beats%20Executive.png)