# Skullcandy Push
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.4; 25 -10.3; 28 -10.2; 31 -10.0; 34 -9.9; 37 -9.7; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.2; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.3; 116 -11.4; 128 -11.5; 141 -11.5; 155 -11.4; 170 -11.0; 187 -10.4; 206 -9.8; 227 -9.2; 249 -8.6; 274 -8.0; 302 -7.3; 332 -6.7; 365 -6.1; 402 -5.5; 442 -4.8; 486 -4.1; 535 -3.4; 588 -2.6; 647 -1.9; 712 -1.3; 783 -0.8; 861 -0.5; 947 -0.7; 1042 -1.3; 1146 -2.1; 1261 -2.9; 1387 -3.2; 1526 -3.3; 1678 -3.5; 1846 -3.7; 2031 -4.0; 2234 -3.8; 2457 -3.2; 2703 -3.0; 2973 -2.7; 3270 -2.7; 3597 -3.1; 3957 -4.0; 4353 -5.3; 4788 -6.3; 5267 -7.8; 5793 -8.6; 6373 -8.2; 7010 -7.6; 7711 -9.2; 8482 -6.8; 9330 -1.8; 10263 -1.0; 11289 -1.0; 12418 -2.1; 13660 -5.4; 15026 -3.5; 16529 -1.1; 18182 -1.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Push GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Push ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 1.32 | -9.3 dB |
| Peaking | 21 Hz    | 0.18 | -7.0 dB |
| Peaking | 163 Hz   | 0.57 | -7.9 dB |
| Peaking | 6194 Hz  | 1.07 | -7.7 dB |
| Peaking | 21063 Hz | 1.44 | -2.2 dB |
| Peaking | 839 Hz   | 2.51 | 2.2 dB  |
| Peaking | 1739 Hz  | 1.54 | -2.2 dB |
| Peaking | 8044 Hz  | 4.01 | -5.5 dB |
| Peaking | 9835 Hz  | 1.08 | 4.1 dB  |
| Peaking | 13757 Hz | 2.7  | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Push/Skullcandy%20Push.png)