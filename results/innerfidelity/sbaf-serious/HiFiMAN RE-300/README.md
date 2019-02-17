# HiFiMAN RE-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.7; 25 -6.8; 28 -6.9; 31 -7.0; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.5; 49 -7.7; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.2; 87 -9.5; 96 -10.0; 106 -10.2; 116 -10.4; 128 -10.5; 141 -10.8; 155 -10.8; 170 -10.9; 187 -10.8; 206 -10.7; 227 -10.5; 249 -10.3; 274 -10.0; 302 -9.7; 332 -9.3; 365 -8.9; 402 -8.4; 442 -7.8; 486 -7.5; 535 -7.0; 588 -6.3; 647 -5.9; 712 -5.8; 783 -5.4; 861 -5.7; 947 -6.1; 1042 -6.9; 1146 -7.0; 1261 -7.3; 1387 -8.9; 1526 -10.0; 1678 -9.8; 1846 -8.2; 2031 -5.2; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -4.1; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 100 Hz  | 0.77 | -1.3 dB |
| Peaking | 200 Hz  | 0.56 | -3.8 dB |
| Peaking | 684 Hz  | 1.91 | 1.5 dB  |
| Peaking | 1622 Hz | 2.22 | -7.6 dB |
| Peaking | 3088 Hz | 0.71 | 7.6 dB  |
| Peaking | 1944 Hz | 6.44 | -1.0 dB |
| Peaking | 2321 Hz | 4.7  | 1.9 dB  |
| Peaking | 3203 Hz | 2.72 | -1.1 dB |
| Peaking | 5555 Hz | 2.75 | 3.5 dB  |
| Peaking | 7598 Hz | 1.09 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-300/HiFiMAN%20RE-300.png)