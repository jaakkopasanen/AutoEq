# Turtle Beach Recon 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.2; 28 -9.2; 31 -9.1; 34 -8.8; 37 -8.5; 41 -8.0; 45 -7.5; 49 -7.1; 54 -6.9; 60 -7.0; 66 -7.6; 72 -8.5; 79 -9.6; 87 -10.8; 96 -11.8; 106 -12.4; 116 -12.5; 128 -12.2; 141 -11.7; 155 -11.0; 170 -10.1; 187 -9.1; 206 -7.9; 227 -6.6; 249 -5.4; 274 -4.2; 302 -2.9; 332 -1.7; 365 -1.2; 402 -1.4; 442 -2.1; 486 -2.3; 535 -2.1; 588 -2.1; 647 -2.0; 712 -2.0; 783 -1.8; 861 -1.5; 947 -0.5; 1042 -1.3; 1146 -1.4; 1261 -0.5; 1387 -2.3; 1526 -2.7; 1678 -2.8; 1846 -3.4; 2031 -3.8; 2234 -4.2; 2457 -4.3; 2703 -4.3; 2973 -4.7; 3270 -5.6; 3597 -6.0; 3957 -6.1; 4353 -5.5; 4788 -2.4; 5267 -3.1; 5793 -5.2; 6373 -6.7; 7010 -7.8; 7711 -6.9; 8482 -6.2; 9330 -5.7; 10263 -6.5; 11289 -7.8; 12418 -6.3; 13660 -5.2; 15026 -5.9; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.38 | -4.3 dB |
| Peaking | 124 Hz  | 0.94 | -8.1 dB |
| Peaking | 357 Hz  | 1.53 | 4.3 dB  |
| Peaking | 1018 Hz | 1.02 | 3.8 dB  |
| Peaking | 9794 Hz | 0.83 | -2.1 dB |
| Peaking | 60 Hz   | 4.92 | 1.2 dB  |
| Peaking | 4192 Hz | 2.6  | -2.8 dB |
| Peaking | 4896 Hz | 3.81 | 4.9 dB  |
| Peaking | 6828 Hz | 3.97 | -2.1 dB |
| Peaking | 9203 Hz | 5.84 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Recon%20200/Turtle%20Beach%20Recon%20200.png)