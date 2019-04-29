# Campfire Audio Andromeda sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.6; 25 -6.7; 28 -6.8; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.2; 45 -7.4; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.1; 72 -8.5; 79 -8.8; 87 -9.2; 96 -9.6; 106 -10.0; 116 -10.3; 128 -10.6; 141 -10.8; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.2; 227 -11.1; 249 -11.0; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.0; 402 -9.7; 442 -9.3; 486 -8.9; 535 -8.4; 588 -7.9; 647 -7.3; 712 -6.6; 783 -5.9; 861 -5.3; 947 -4.9; 1042 -4.8; 1146 -5.3; 1261 -5.8; 1387 -6.1; 1526 -5.9; 1678 -5.4; 1846 -4.8; 2031 -3.9; 2234 -2.8; 2457 -1.6; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -0.7; 5793 -0.5; 6373 -3.5; 7010 -7.8; 7711 -8.9; 8482 -10.1; 9330 -9.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -10.8; 16529 -11.4; 18182 -10.7; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 209 Hz   |  0.44 | -4.8 dB  |
| Peaking | 875 Hz   |  3.04 | 2.0 dB   |
| Peaking | 5794 Hz  |  0.49 | 9.4 dB   |
| Peaking | 7991 Hz  |  1.64 | -11.1 dB |
| Peaking | 16768 Hz |  0.81 | -6.2 dB  |
| Peaking | 1621 Hz  |  2.26 | -1.7 dB  |
| Peaking | 2680 Hz  |  4.32 | 1.4 dB   |
| Peaking | 3315 Hz  |  0.19 | 0.3 dB   |
| Peaking | 4760 Hz  |  6.43 | -1.6 dB  |
| Peaking | 9012 Hz  | 10.78 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Andromeda%20sample%201/Campfire%20Audio%20Andromeda%20sample%201.png)