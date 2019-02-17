# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -0.9; 34 -0.9; 37 -0.9; 41 -1.0; 45 -1.3; 49 -1.5; 54 -1.8; 60 -2.2; 66 -2.6; 72 -2.9; 79 -3.1; 87 -3.5; 96 -4.1; 106 -4.5; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.7; 170 -5.7; 187 -5.5; 206 -5.4; 227 -5.8; 249 -6.1; 274 -6.3; 302 -6.3; 332 -6.2; 365 -6.1; 402 -6.1; 442 -6.3; 486 -6.5; 535 -6.4; 588 -6.2; 647 -6.0; 712 -5.9; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.5; 1146 -6.8; 1261 -7.0; 1387 -7.1; 1526 -6.7; 1678 -6.5; 1846 -6.8; 2031 -6.9; 2234 -6.6; 2457 -5.7; 2703 -6.0; 2973 -6.1; 3270 -6.4; 3597 -6.4; 3957 -4.7; 4353 -2.5; 4788 -1.7; 5267 -1.6; 5793 -0.7; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -10.1; 11289 -12.2; 12418 -12.8; 13660 -17.9; 15026 -25.5; 16529 -30.3; 18182 -29.8; 20000 -24.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.66 | 4.5 dB   |
| Peaking | 45 Hz    | 0.64 | 3.8 dB   |
| Peaking | 82 Hz    | 3.35 | 0.4 dB   |
| Peaking | 7417 Hz  | 0.65 | 11.3 dB  |
| Peaking | 17567 Hz | 0.4  | -26.7 dB |
| Peaking | 1858 Hz  | 1.39 | -1.1 dB  |
| Peaking | 3516 Hz  | 3.23 | -2.8 dB  |
| Peaking | 5489 Hz  | 1.17 | 2.8 dB   |
| Peaking | 7596 Hz  | 4.07 | -4.4 dB  |
| Peaking | 12589 Hz | 5.99 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB   |
| Peaking | 62 Hz    | 1.41 | 3.2 dB   |
| Peaking | 125 Hz   | 1.41 | 0.6 dB   |
| Peaking | 250 Hz   | 1.41 | 0.2 dB   |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 16000 Hz | 1.41 | -32.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine/Audeze%20Sine.png)