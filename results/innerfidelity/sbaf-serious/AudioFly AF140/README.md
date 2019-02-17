# AudioFly AF140
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.1; 25 -10.3; 28 -10.6; 31 -10.8; 34 -11.0; 37 -11.2; 41 -11.5; 45 -11.7; 49 -11.9; 54 -12.1; 60 -12.4; 66 -12.6; 72 -13.0; 79 -13.3; 87 -13.6; 96 -13.9; 106 -14.1; 116 -14.2; 128 -14.4; 141 -14.5; 155 -14.5; 170 -14.4; 187 -14.2; 206 -14.0; 227 -13.6; 249 -13.3; 274 -12.8; 302 -12.3; 332 -11.8; 365 -11.1; 402 -10.5; 442 -9.6; 486 -9.4; 535 -8.6; 588 -7.6; 647 -6.9; 712 -5.7; 783 -5.0; 861 -5.2; 947 -5.7; 1042 -6.7; 1146 -7.5; 1261 -8.4; 1387 -9.5; 1526 -10.5; 1678 -11.3; 1846 -11.9; 2031 -11.8; 2234 -11.6; 2457 -10.5; 2703 -8.6; 2973 -5.5; 3270 -2.8; 3597 -1.8; 3957 -0.6; 4353 -0.5; 4788 -1.7; 5267 -6.9; 5793 -5.6; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -9.2; 11289 -8.5; 12418 -6.5; 13660 -8.1; 15026 -10.6; 16529 -7.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF140 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.37 | -5.8 dB |
| Peaking | 209 Hz   | 0.84 | -4.8 dB |
| Peaking | 2113 Hz  | 1.72 | -7.0 dB |
| Peaking | 3729 Hz  | 1.82 | 6.2 dB  |
| Peaking | 4487 Hz  | 5.53 | 2.8 dB  |
| Peaking | 810 Hz   | 1.65 | 5.5 dB  |
| Peaking | 812 Hz   | 0.71 | -2.7 dB |
| Peaking | 6460 Hz  | 9.44 | 5.1 dB  |
| Peaking | 10557 Hz | 5.81 | -3.2 dB |
| Peaking | 15118 Hz | 3.2  | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF140/AudioFly%20AF140.png)