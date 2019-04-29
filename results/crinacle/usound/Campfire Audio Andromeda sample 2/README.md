# Campfire Audio Andromeda sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -4.9; 28 -5.4; 31 -5.7; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.8; 49 -7.1; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.6; 106 -10.0; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.2; 187 -11.3; 206 -11.4; 227 -11.3; 249 -11.1; 274 -11.0; 302 -10.9; 332 -10.6; 365 -10.4; 402 -10.0; 442 -9.7; 486 -9.3; 535 -8.9; 588 -8.4; 647 -7.8; 712 -7.1; 783 -6.4; 861 -5.8; 947 -5.4; 1042 -5.5; 1146 -5.9; 1261 -6.4; 1387 -6.6; 1526 -6.4; 1678 -5.8; 1846 -4.9; 2031 -3.6; 2234 -2.2; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -1.8; 5793 -1.4; 6373 -5.4; 7010 -8.9; 7711 -9.0; 8482 -8.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.96 | 2.6 dB  |
| Peaking | 138 Hz  | 0.7  | -3.4 dB |
| Peaking | 316 Hz  | 0.79 | -3.2 dB |
| Peaking | 3796 Hz | 0.77 | 6.9 dB  |
| Peaking | 7567 Hz | 2.78 | -5.7 dB |
| Peaking | 962 Hz  | 2.04 | 2.1 dB  |
| Peaking | 1494 Hz | 1.9  | -1.2 dB |
| Peaking | 2256 Hz | 0.35 | -1.1 dB |
| Peaking | 2473 Hz | 2.52 | 2.7 dB  |
| Peaking | 5794 Hz | 7.94 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Andromeda%20sample%202/Campfire%20Audio%20Andromeda%20sample%202.png)