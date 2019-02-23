# Polk Audio Hinge
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.4; 25 -12.6; 28 -12.7; 31 -12.8; 34 -12.9; 37 -13.0; 41 -13.0; 45 -13.1; 49 -13.1; 54 -13.2; 60 -13.4; 66 -13.4; 72 -13.4; 79 -13.5; 87 -13.5; 96 -14.1; 106 -14.3; 116 -14.9; 128 -15.1; 141 -15.5; 155 -15.1; 170 -14.5; 187 -14.1; 206 -13.0; 227 -11.5; 249 -10.0; 274 -8.4; 302 -8.3; 332 -8.3; 365 -8.0; 402 -8.2; 442 -8.5; 486 -8.6; 535 -8.1; 588 -7.2; 647 -6.2; 712 -5.4; 783 -3.9; 861 -2.4; 947 -0.8; 1042 -0.5; 1146 -1.7; 1261 -4.5; 1387 -6.1; 1526 -7.8; 1678 -7.4; 1846 -6.8; 2031 -8.3; 2234 -7.3; 2457 -5.5; 2703 -4.2; 2973 -3.5; 3270 -3.6; 3597 -2.0; 3957 -1.0; 4353 -3.9; 4788 -5.3; 5267 -2.1; 5793 -0.5; 6373 -1.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Hinge GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Hinge ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.27 | -6.2 dB |
| Peaking | 151 Hz  | 1.32 | -5.0 dB |
| Peaking | 986 Hz  | 3.35 | 7.0 dB  |
| Peaking | 4904 Hz | 1.16 | 4.3 dB  |
| Peaking | 2005 Hz | 1.56 | -4.3 dB |
| Peaking | 4125 Hz | 0.54 | 4.2 dB  |
| Peaking | 4707 Hz | 5.37 | -6.1 dB |
| Peaking | 6115 Hz | 3.74 | 3.5 dB  |
| Peaking | 7222 Hz | 1.04 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Hinge/Polk%20Audio%20Hinge.png)