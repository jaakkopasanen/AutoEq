# Philips SBC HP910
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -2.1; 45 -2.7; 49 -3.2; 54 -4.0; 60 -4.5; 66 -4.7; 72 -5.3; 79 -5.1; 87 -5.4; 96 -6.6; 106 -7.2; 116 -7.6; 128 -7.9; 141 -8.0; 155 -8.0; 170 -7.7; 187 -7.8; 206 -7.7; 227 -7.5; 249 -7.2; 274 -6.9; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.6; 442 -5.3; 486 -5.3; 535 -5.2; 588 -5.4; 647 -4.6; 712 -5.3; 783 -5.5; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -7.1; 1387 -7.2; 1526 -7.3; 1678 -7.8; 1846 -8.3; 2031 -8.5; 2234 -9.7; 2457 -10.5; 2703 -11.5; 2973 -12.0; 3270 -10.6; 3597 -8.5; 3957 -7.5; 4353 -6.6; 4788 -10.6; 5267 -9.6; 5793 -6.3; 6373 -9.7; 7010 -13.1; 7711 -14.0; 8482 -15.0; 9330 -12.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SBC HP910 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SBC HP910 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 28 Hz    |  1.1  | 6.8 dB   |
| Peaking | 2529 Hz  |  0.59 | -5.6 dB  |
| Peaking | 2882 Hz  |  3.67 | -3.6 dB  |
| Peaking | 3391 Hz  |  0.21 | 3.7 dB   |
| Peaking | 8057 Hz  |  2.11 | -10.7 dB |
| Peaking | 163 Hz   |  1.25 | -2.0 dB  |
| Peaking | 537 Hz   |  1.8  | 0.9 dB   |
| Peaking | 4867 Hz  |  2.83 | 3.4 dB   |
| Peaking | 4887 Hz  |  7.18 | -7.2 dB  |
| Peaking | 10284 Hz | 10.56 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SBC%20HP910/Philips%20SBC%20HP910.png)