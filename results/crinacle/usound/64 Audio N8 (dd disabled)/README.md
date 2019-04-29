# 64 Audio N8 (dd disabled)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.3; 106 -2.3; 116 -3.3; 128 -4.1; 141 -5.0; 155 -5.6; 170 -6.3; 187 -6.9; 206 -7.5; 227 -7.9; 249 -8.1; 274 -8.4; 302 -8.6; 332 -8.7; 365 -8.7; 402 -8.7; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.2; 647 -8.0; 712 -7.6; 783 -7.3; 861 -6.9; 947 -6.8; 1042 -7.1; 1146 -7.9; 1261 -8.9; 1387 -9.7; 1526 -10.0; 1678 -9.9; 1846 -9.5; 2031 -9.1; 2234 -8.5; 2457 -7.6; 2703 -6.6; 2973 -5.6; 3270 -4.8; 3597 -4.4; 3957 -5.0; 4353 -5.5; 4788 -6.0; 5267 -4.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.8; 16529 -17.2; 18182 -18.5; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 (dd disabled) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 (dd disabled) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 58 Hz    | 0.25 | 7.3 dB   |
| Peaking | 242 Hz   | 0.58 | -5.5 dB  |
| Peaking | 1629 Hz  | 2.26 | -3.7 dB  |
| Peaking | 6080 Hz  | 3.1  | 6.4 dB   |
| Peaking | 17791 Hz | 1.32 | -14.0 dB |
| Peaking | 19 Hz    | 2.61 | 0.8 dB   |
| Peaking | 3487 Hz  | 2.33 | 4.4 dB   |
| Peaking | 3673 Hz  | 1.05 | -2.3 dB  |
| Peaking | 13509 Hz | 1.85 | 3.2 dB   |
| Peaking | 15719 Hz | 2.68 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.7 dB   |
| Peaking | 125 Hz   | 1.41 | 2.3 dB   |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20(dd%20disabled)/64%20Audio%20N8%20(dd%20disabled).png)