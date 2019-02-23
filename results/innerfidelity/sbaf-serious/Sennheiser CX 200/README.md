# Sennheiser CX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.3; 28 -8.7; 31 -9.0; 34 -9.2; 37 -9.3; 41 -9.5; 45 -9.7; 49 -9.9; 54 -10.1; 60 -10.2; 66 -10.5; 72 -10.6; 79 -10.8; 87 -11.0; 96 -11.2; 106 -11.2; 116 -11.1; 128 -11.1; 141 -11.0; 155 -10.8; 170 -10.6; 187 -10.3; 206 -10.1; 227 -9.6; 249 -9.3; 274 -8.9; 302 -8.6; 332 -8.2; 365 -7.8; 402 -7.4; 442 -6.9; 486 -6.7; 535 -6.4; 588 -5.9; 647 -5.7; 712 -5.7; 783 -5.5; 861 -5.8; 947 -6.1; 1042 -6.4; 1146 -7.0; 1261 -7.2; 1387 -7.9; 1526 -8.3; 1678 -8.4; 1846 -7.9; 2031 -7.1; 2234 -5.9; 2457 -3.9; 2703 -2.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -3.9; 5267 -4.2; 5793 -5.1; 6373 -6.3; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -7.5; 12418 -6.5; 13660 -6.9; 15026 -8.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.56 | -3.0 dB |
| Peaking | 124 Hz   | 1.03 | -2.9 dB |
| Peaking | 223 Hz   | 1.64 | -1.8 dB |
| Peaking | 1735 Hz  | 2.39 | -3.2 dB |
| Peaking | 3386 Hz  | 1.6  | 6.9 dB  |
| Peaking | 744 Hz   | 2.04 | 1.3 dB  |
| Peaking | 1309 Hz  | 3.37 | -0.6 dB |
| Peaking | 4047 Hz  | 9.2  | 1.0 dB  |
| Peaking | 9577 Hz  | 0.9  | -0.6 dB |
| Peaking | 14809 Hz | 5.69 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20CX%20200/Sennheiser%20CX%20200.png)