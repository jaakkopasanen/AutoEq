# Campfire Audio Andromeda sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.7; 31 -6.9; 34 -7.1; 37 -7.2; 41 -7.3; 45 -7.5; 49 -7.7; 54 -8.0; 60 -8.2; 66 -8.4; 72 -8.7; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.2; 116 -10.6; 128 -10.9; 141 -11.1; 155 -11.2; 170 -11.4; 187 -11.5; 206 -11.5; 227 -11.4; 249 -11.2; 274 -11.1; 302 -10.9; 332 -10.6; 365 -10.3; 402 -10.0; 442 -9.6; 486 -9.2; 535 -8.7; 588 -8.2; 647 -7.6; 712 -6.9; 783 -6.1; 861 -5.5; 947 -5.1; 1042 -5.0; 1146 -5.4; 1261 -5.9; 1387 -6.2; 1526 -6.1; 1678 -5.7; 1846 -5.0; 2031 -4.1; 2234 -2.7; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.8; 5267 -0.6; 5793 -0.6; 6373 -3.9; 7010 -5.8; 7711 -6.4; 8482 -7.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -10.1; 16529 -11.5; 18182 -10.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 158 Hz   | 0.63 | -4.6 dB |
| Peaking | 351 Hz   | 1.36 | -2.2 dB |
| Peaking | 3219 Hz  | 1.19 | 6.5 dB  |
| Peaking | 5512 Hz  | 4.32 | 4.4 dB  |
| Peaking | 16866 Hz | 1.26 | -5.5 dB |
| Peaking | 18 Hz    | 1.91 | 0.9 dB  |
| Peaking | 963 Hz   | 3.12 | 1.7 dB  |
| Peaking | 1543 Hz  | 3.32 | -1.1 dB |
| Peaking | 8372 Hz  | 4.53 | -1.8 dB |
| Peaking | 12896 Hz | 3.63 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Andromeda%20sample%203/Campfire%20Audio%20Andromeda%20sample%203.png)