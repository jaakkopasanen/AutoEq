# Fidue A31s
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.6; 25 -13.7; 28 -13.9; 31 -14.1; 34 -14.2; 37 -14.3; 41 -14.4; 45 -14.5; 49 -14.6; 54 -14.6; 60 -14.7; 66 -14.8; 72 -14.8; 79 -14.9; 87 -15.0; 96 -15.1; 106 -14.8; 116 -14.7; 128 -14.6; 141 -14.3; 155 -14.0; 170 -13.7; 187 -13.2; 206 -12.7; 227 -12.2; 249 -11.6; 274 -11.0; 302 -10.4; 332 -9.8; 365 -9.1; 402 -8.5; 442 -7.7; 486 -7.3; 535 -6.7; 588 -5.9; 647 -5.5; 712 -5.3; 783 -4.7; 861 -5.1; 947 -5.4; 1042 -5.4; 1146 -5.9; 1261 -6.6; 1387 -7.2; 1526 -7.4; 1678 -8.7; 1846 -10.0; 2031 -10.7; 2234 -11.3; 2457 -9.9; 2703 -7.5; 2973 -4.3; 3270 -2.6; 3597 -2.5; 3957 -5.3; 4353 -10.0; 4788 -7.1; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A31s GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A31s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.32 | -7.9 dB |
| Peaking | 159 Hz  | 0.84 | -4.4 dB |
| Peaking | 2175 Hz | 2.88 | -5.5 dB |
| Peaking | 3298 Hz | 5.18 | 5.4 dB  |
| Peaking | 5938 Hz | 4.3  | 7.0 dB  |
| Peaking | 304 Hz  | 2.24 | -1.0 dB |
| Peaking | 769 Hz  | 1.64 | 2.3 dB  |
| Peaking | 4476 Hz | 8.51 | -5.7 dB |
| Peaking | 5220 Hz | 9.72 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A31s/Fidue%20A31s.png)