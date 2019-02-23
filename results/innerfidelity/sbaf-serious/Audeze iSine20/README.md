# Audeze iSine20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -2.9; 28 -2.9; 31 -3.0; 34 -3.0; 37 -3.1; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.7; 60 -4.0; 66 -4.3; 72 -4.6; 79 -5.0; 87 -5.4; 96 -5.9; 106 -6.2; 116 -6.5; 128 -6.9; 141 -7.2; 155 -7.5; 170 -7.7; 187 -7.9; 206 -8.1; 227 -8.1; 249 -8.3; 274 -8.3; 302 -8.4; 332 -8.6; 365 -8.7; 402 -8.8; 442 -8.8; 486 -9.2; 535 -9.4; 588 -9.4; 647 -9.7; 712 -10.3; 783 -10.6; 861 -11.1; 947 -11.7; 1042 -12.3; 1146 -12.7; 1261 -12.5; 1387 -12.8; 1526 -14.1; 1678 -13.5; 1846 -11.4; 2031 -9.0; 2234 -6.5; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.8; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.7; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.8  | 3.6 dB   |
| Peaking | 56 Hz    | 1.38 | 1.8 dB   |
| Peaking | 1661 Hz  | 0.5  | -24.1 dB |
| Peaking | 2757 Hz  | 0.39 | 22.5 dB  |
| Peaking | 9974 Hz  | 1.02 | -5.8 dB  |
| Peaking | 2568 Hz  | 7.52 | 2.5 dB   |
| Peaking | 3265 Hz  | 1.16 | -1.2 dB  |
| Peaking | 6190 Hz  | 2.03 | 3.7 dB   |
| Peaking | 7110 Hz  | 4    | -4.4 dB  |
| Peaking | 16351 Hz | 1.62 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -6.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20iSine20/Audeze%20iSine20.png)