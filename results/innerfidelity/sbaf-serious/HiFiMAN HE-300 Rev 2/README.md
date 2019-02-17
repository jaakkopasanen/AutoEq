# HiFiMAN HE-300 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.2; 31 -3.4; 34 -4.5; 37 -5.5; 41 -6.6; 45 -7.5; 49 -8.1; 54 -8.6; 60 -9.1; 66 -9.4; 72 -10.2; 79 -10.9; 87 -11.1; 96 -11.6; 106 -11.8; 116 -11.7; 128 -11.6; 141 -11.2; 155 -10.8; 170 -10.2; 187 -9.9; 206 -9.4; 227 -9.2; 249 -9.9; 274 -9.2; 302 -8.5; 332 -7.9; 365 -7.4; 402 -7.0; 442 -6.5; 486 -6.2; 535 -5.6; 588 -4.9; 647 -4.8; 712 -4.4; 783 -5.0; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.5; 1261 -8.1; 1387 -9.1; 1526 -10.0; 1678 -10.4; 1846 -10.5; 2031 -11.3; 2234 -10.8; 2457 -10.2; 2703 -10.3; 2973 -11.6; 3270 -12.4; 3597 -11.1; 3957 -10.4; 4353 -11.6; 4788 -12.6; 5267 -11.4; 5793 -7.5; 6373 -4.8; 7010 -5.7; 7711 -6.2; 8482 -6.9; 9330 -9.8; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.45 | 6.8 dB  |
| Peaking | 109 Hz   | 0.72 | -5.6 dB |
| Peaking | 1912 Hz  | 2.08 | -3.8 dB |
| Peaking | 3816 Hz  | 1.35 | -5.2 dB |
| Peaking | 21317 Hz | 2.41 | -3.8 dB |
| Peaking | 260 Hz   | 4.81 | -1.5 dB |
| Peaking | 668 Hz   | 2.22 | 2.7 dB  |
| Peaking | 5141 Hz  | 4.13 | -5.3 dB |
| Peaking | 6183 Hz  | 1.96 | 4.2 dB  |
| Peaking | 9555 Hz  | 5.7  | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300%20Rev%202/HiFiMAN%20HE-300%20Rev%202.png)