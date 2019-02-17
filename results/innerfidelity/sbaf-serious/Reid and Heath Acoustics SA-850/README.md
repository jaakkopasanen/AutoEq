# Reid and Heath Acoustics SA-850
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.0; 28 -2.1; 31 -3.1; 34 -3.9; 37 -4.5; 41 -5.1; 45 -5.4; 49 -5.6; 54 -5.6; 60 -5.7; 66 -5.7; 72 -5.8; 79 -5.9; 87 -6.0; 96 -6.0; 106 -5.8; 116 -6.0; 128 -6.5; 141 -6.9; 155 -7.2; 170 -7.3; 187 -7.6; 206 -8.1; 227 -9.1; 249 -9.5; 274 -9.8; 302 -9.7; 332 -9.3; 365 -9.5; 402 -10.0; 442 -10.3; 486 -10.9; 535 -11.3; 588 -11.0; 647 -10.8; 712 -10.0; 783 -8.5; 861 -7.2; 947 -6.2; 1042 -6.9; 1146 -8.4; 1261 -9.1; 1387 -10.0; 1526 -11.1; 1678 -10.2; 1846 -8.6; 2031 -6.7; 2234 -5.1; 2457 -2.7; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -5.9; 5267 -9.3; 5793 -8.5; 6373 -8.5; 7010 -9.2; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Reid and Heath Acoustics SA-850 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Reid and Heath Acoustics SA-850 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.96 | 6.3 dB  |
| Peaking | 274 Hz  | 1.69 | -2.8 dB |
| Peaking | 548 Hz  | 1.82 | -4.7 dB |
| Peaking | 1562 Hz | 2.92 | -5.4 dB |
| Peaking | 3178 Hz | 1.95 | 7.4 dB  |
| Peaking | 696 Hz  | 7.22 | -1.1 dB |
| Peaking | 937 Hz  | 6.28 | 1.9 dB  |
| Peaking | 4058 Hz | 5.13 | 3.6 dB  |
| Peaking | 4480 Hz | 8.29 | 5.4 dB  |
| Peaking | 5246 Hz | 1.83 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Reid%20and%20Heath%20Acoustics%20SA-850/Reid%20and%20Heath%20Acoustics%20SA-850.png)