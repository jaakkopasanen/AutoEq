# Turtle Beach Recon 50X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.6; 28 -3.9; 31 -4.1; 34 -4.3; 37 -4.3; 41 -4.3; 45 -4.3; 49 -4.2; 54 -4.2; 60 -4.4; 66 -4.9; 72 -5.3; 79 -5.9; 87 -6.5; 96 -6.9; 106 -7.3; 116 -7.8; 128 -8.5; 141 -9.3; 155 -9.9; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.6; 249 -11.0; 274 -11.4; 302 -11.3; 332 -11.4; 365 -11.4; 402 -10.6; 442 -10.4; 486 -10.5; 535 -10.4; 588 -10.3; 647 -10.0; 712 -9.2; 783 -7.9; 861 -6.7; 947 -6.0; 1042 -5.9; 1146 -5.7; 1261 -5.5; 1387 -4.7; 1526 -3.7; 1678 -3.2; 1846 -3.0; 2031 -2.9; 2234 -2.5; 2457 -1.8; 2703 -2.5; 2973 -4.2; 3270 -4.7; 3597 -4.5; 3957 -4.1; 4353 -2.4; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -5.1; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 50X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 50X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.3  | 3.1 dB  |
| Peaking | 251 Hz  | 0.53 | -5.2 dB |
| Peaking | 595 Hz  | 2.54 | -1.9 dB |
| Peaking | 2037 Hz | 1.01 | 4.3 dB  |
| Peaking | 5169 Hz | 3.32 | 6.2 dB  |
| Peaking | 906 Hz  | 1.56 | -0.9 dB |
| Peaking | 923 Hz  | 3.21 | 1.7 dB  |
| Peaking | 943 Hz  | 2.36 | 0.1 dB  |
| Peaking | 5892 Hz | 8.89 | 3.2 dB  |
| Peaking | 6581 Hz | 3.22 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Recon%2050X/Turtle%20Beach%20Recon%2050X.png)