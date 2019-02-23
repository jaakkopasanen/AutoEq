# V-Moda Crossfade Wireless Wired Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -5.0; 25 -5.6; 28 -6.5; 31 -7.3; 34 -7.9; 37 -8.4; 41 -9.0; 45 -9.5; 49 -9.8; 54 -10.1; 60 -10.3; 66 -10.2; 72 -9.8; 79 -10.8; 87 -12.1; 96 -11.8; 106 -11.7; 116 -12.6; 128 -13.1; 141 -13.2; 155 -13.0; 170 -12.3; 187 -12.2; 206 -11.5; 227 -10.2; 249 -8.7; 274 -7.0; 302 -5.3; 332 -3.5; 365 -1.4; 402 -0.5; 442 -0.7; 486 -0.5; 535 -0.5; 588 -0.6; 647 -1.5; 712 -2.8; 783 -3.8; 861 -5.1; 947 -6.2; 1042 -7.1; 1146 -7.7; 1261 -8.3; 1387 -8.9; 1526 -9.4; 1678 -9.6; 1846 -9.2; 2031 -8.7; 2234 -8.9; 2457 -8.8; 2703 -7.8; 2973 -8.7; 3270 -10.0; 3597 -10.9; 3957 -7.9; 4353 -5.2; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -11.1; 10263 -9.8; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Wired Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Wired Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 176 Hz  |  0.5  | -10.1 dB |
| Peaking | 448 Hz  |  0.68 | 12.9 dB  |
| Peaking | 2039 Hz |  0.32 | -4.9 dB  |
| Peaking | 5585 Hz |  1.9  | 10.0 dB  |
| Peaking | 9339 Hz |  3.86 | -5.3 dB  |
| Peaking | 16 Hz   |  1.36 | 4.0 dB   |
| Peaking | 43 Hz   |  2.1  | -1.3 dB  |
| Peaking | 2690 Hz |  3.6  | 2.1 dB   |
| Peaking | 3549 Hz |  4.37 | -3.4 dB  |
| Peaking | 4708 Hz | 10.61 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 8.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Wired%20Mode/V-Moda%20Crossfade%20Wireless%20Wired%20Mode.png)