# Campfire Audio Andromeda SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.3; 25 -3.7; 28 -4.2; 31 -4.5; 34 -4.9; 37 -5.1; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.5; 60 -6.9; 66 -7.3; 72 -7.7; 79 -8.1; 87 -8.6; 96 -9.0; 106 -9.4; 116 -9.9; 128 -10.2; 141 -10.5; 155 -10.7; 170 -10.9; 187 -11.0; 206 -11.1; 227 -11.1; 249 -11.0; 274 -10.9; 302 -10.8; 332 -10.7; 365 -10.5; 402 -10.3; 442 -10.0; 486 -9.7; 535 -9.4; 588 -9.1; 647 -8.6; 712 -8.1; 783 -7.5; 861 -6.9; 947 -6.4; 1042 -6.2; 1146 -6.4; 1261 -6.5; 1387 -6.4; 1526 -5.9; 1678 -5.6; 1846 -5.2; 2031 -4.7; 2234 -3.5; 2457 -1.9; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.0; 7010 -6.9; 7711 -7.6; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.7; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.29 | 4.5 dB  |
| Peaking | 227 Hz   | 0.39 | -4.8 dB |
| Peaking | 4767 Hz  | 0.6  | 7.8 dB  |
| Peaking | 7530 Hz  | 3.32 | -5.2 dB |
| Peaking | 10169 Hz | 0.72 | -2.3 dB |
| Peaking | 952 Hz   | 2.88 | 1.2 dB  |
| Peaking | 2162 Hz  | 0.91 | -1.7 dB |
| Peaking | 2723 Hz  | 2.43 | 3.1 dB  |
| Peaking | 4912 Hz  | 1.11 | -0.6 dB |
| Peaking | 5987 Hz  | 6.83 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Andromeda%20SS/Campfire%20Audio%20Andromeda%20SS.png)