# Kennerton Odin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.6; 34 -3.7; 37 -4.7; 41 -5.8; 45 -6.7; 49 -7.4; 54 -8.0; 60 -8.4; 66 -8.8; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.3; 106 -9.3; 116 -9.3; 128 -9.3; 141 -9.3; 155 -9.2; 170 -9.0; 187 -9.0; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.8; 302 -9.1; 332 -9.2; 365 -8.7; 402 -8.3; 442 -8.5; 486 -7.9; 535 -6.6; 588 -6.3; 647 -7.2; 712 -8.0; 783 -8.7; 861 -9.0; 947 -8.6; 1042 -7.3; 1146 -5.8; 1261 -5.3; 1387 -5.0; 1526 -3.9; 1678 -1.7; 1846 -0.5; 2031 -0.5; 2234 -1.3; 2457 -2.6; 2703 -3.6; 2973 -4.4; 3270 -5.0; 3597 -5.4; 3957 -5.4; 4353 -5.4; 4788 -5.7; 5267 -7.7; 5793 -9.5; 6373 -8.7; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -9.0; 13660 -7.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Odin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Odin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.93 | 8.0 dB  |
| Peaking | 72 Hz    | 0.35 | -3.7 dB |
| Peaking | 335 Hz   | 2.11 | -1.7 dB |
| Peaking | 875 Hz   | 3.22 | -3.1 dB |
| Peaking | 1986 Hz  | 1.85 | 6.5 dB  |
| Peaking | 458 Hz   | 7.88 | -0.9 dB |
| Peaking | 563 Hz   | 7.37 | 1.3 dB  |
| Peaking | 5874 Hz  | 3.8  | -5.8 dB |
| Peaking | 5891 Hz  | 1.37 | 2.2 dB  |
| Peaking | 12653 Hz | 3.9  | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kennerton%20Odin/Kennerton%20Odin.png)