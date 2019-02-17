# Audeze Mobius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.0; 25 -6.7; 28 -6.5; 31 -6.3; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.3; 49 -6.1; 54 -5.8; 60 -5.5; 66 -5.5; 72 -5.4; 79 -5.4; 87 -5.4; 96 -5.6; 106 -5.7; 116 -5.9; 128 -6.0; 141 -6.2; 155 -6.4; 170 -6.5; 187 -6.5; 206 -6.5; 227 -6.4; 249 -6.3; 274 -6.1; 302 -5.9; 332 -5.5; 365 -5.2; 402 -4.8; 442 -4.5; 486 -5.0; 535 -5.6; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.8; 861 -5.7; 947 -5.3; 1042 -5.1; 1146 -5.5; 1261 -5.8; 1387 -5.6; 1526 -5.9; 1678 -6.6; 1846 -7.3; 2031 -7.2; 2234 -6.5; 2457 -6.3; 2703 -6.9; 2973 -7.4; 3270 -7.9; 3597 -6.2; 3957 -0.8; 4353 -0.7; 4788 -0.5; 5267 -1.0; 5793 -0.8; 6373 -0.7; 7010 -2.8; 7711 -5.9; 8482 -9.0; 9330 -8.3; 10263 -6.4; 11289 -5.7; 12418 -5.1; 13660 -5.3; 15026 -9.8; 16529 -14.1; 18182 -15.4; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Mobius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Mobius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.05 | -1.0 dB  |
| Peaking | 2902 Hz  | 0.67 | -11.9 dB |
| Peaking | 6086 Hz  | 0.34 | 15.4 dB  |
| Peaking | 8601 Hz  | 1.7  | -12.7 dB |
| Peaking | 18171 Hz | 0.47 | -13.5 dB |
| Peaking | 20 Hz    | 1.94 | -1.2 dB  |
| Peaking | 429 Hz   | 5.6  | 1.3 dB   |
| Peaking | 2651 Hz  | 3.06 | 2.9 dB   |
| Peaking | 3472 Hz  | 1.8  | -4.1 dB  |
| Peaking | 4021 Hz  | 4.98 | 5.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -9.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20Mobius/Audeze%20Mobius.png)