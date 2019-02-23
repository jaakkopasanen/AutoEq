# Cyberdrive Forte Classic Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.4; 25 -14.4; 28 -14.5; 31 -14.5; 34 -14.5; 37 -14.4; 41 -14.4; 45 -14.4; 49 -14.4; 54 -14.4; 60 -14.5; 66 -14.5; 72 -14.5; 79 -14.6; 87 -14.6; 96 -14.7; 106 -14.5; 116 -14.3; 128 -14.1; 141 -13.8; 155 -13.5; 170 -13.1; 187 -12.6; 206 -12.1; 227 -11.4; 249 -10.9; 274 -10.2; 302 -9.5; 332 -8.8; 365 -8.0; 402 -7.2; 442 -6.4; 486 -5.9; 535 -5.0; 588 -4.1; 647 -3.6; 712 -3.3; 783 -2.3; 861 -2.6; 947 -2.5; 1042 -2.5; 1146 -2.6; 1261 -2.6; 1387 -2.8; 1526 -3.0; 1678 -2.8; 1846 -2.1; 2031 -1.3; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -3.3; 4353 -6.3; 4788 -7.6; 5267 -8.2; 5793 -11.5; 6373 -15.3; 7010 -11.0; 7711 -7.3; 8482 -6.5; 9330 -7.0; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Classic Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Classic Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.13 | -8.5 dB |
| Peaking | 713 Hz  | 0.52 | 6.0 dB  |
| Peaking | 2857 Hz | 1.34 | 5.9 dB  |
| Peaking | 6257 Hz | 3.66 | -9.8 dB |
| Peaking | 2926 Hz | 4.07 | -1.9 dB |
| Peaking | 3616 Hz | 1.88 | 2.4 dB  |
| Peaking | 4438 Hz | 4.3  | -3.2 dB |
| Peaking | 8045 Hz | 7.85 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Classic%20Bass/Cyberdrive%20Forte%20Classic%20Bass.png)