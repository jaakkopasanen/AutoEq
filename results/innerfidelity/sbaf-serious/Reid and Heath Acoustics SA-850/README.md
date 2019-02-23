# Reid and Heath Acoustics SA-850
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.7; 31 -2.7; 34 -3.5; 37 -4.1; 41 -4.6; 45 -4.9; 49 -5.1; 54 -5.2; 60 -5.2; 66 -5.3; 72 -5.3; 79 -5.4; 87 -5.5; 96 -5.6; 106 -5.3; 116 -5.6; 128 -6.0; 141 -6.4; 155 -6.8; 170 -6.9; 187 -7.2; 206 -7.7; 227 -8.6; 249 -9.1; 274 -9.4; 302 -9.2; 332 -8.9; 365 -9.1; 402 -9.6; 442 -9.8; 486 -10.5; 535 -10.9; 588 -10.5; 647 -10.4; 712 -9.6; 783 -8.0; 861 -6.7; 947 -5.8; 1042 -6.5; 1146 -8.0; 1261 -8.6; 1387 -9.6; 1526 -10.7; 1678 -9.8; 1846 -8.2; 2031 -6.2; 2234 -4.6; 2457 -2.3; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -5.5; 5267 -8.8; 5793 -8.0; 6373 -8.0; 7010 -8.8; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 12 Hz   | 0.48 | 8.1 dB  |
| Peaking | 276 Hz  | 1.97 | -2.5 dB |
| Peaking | 545 Hz  | 1.91 | -4.4 dB |
| Peaking | 1565 Hz | 3.14 | -5.1 dB |
| Peaking | 3166 Hz | 1.81 | 7.4 dB  |
| Peaking | 694 Hz  | 6.13 | -1.1 dB |
| Peaking | 936 Hz  | 5.74 | 2.0 dB  |
| Peaking | 4159 Hz | 4.28 | 4.5 dB  |
| Peaking | 4558 Hz | 9.91 | 4.6 dB  |
| Peaking | 5095 Hz | 1.86 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Reid%20and%20Heath%20Acoustics%20SA-850/Reid%20and%20Heath%20Acoustics%20SA-850.png)