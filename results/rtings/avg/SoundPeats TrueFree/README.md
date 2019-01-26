# SoundPeats TrueFree
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -8.3; 23 -8.0; 25 -7.7; 28 -7.3; 31 -6.9; 34 -6.5; 37 -6.2; 41 -5.7; 45 -5.3; 49 -5.0; 54 -4.7; 60 -4.7; 66 -4.7; 72 -4.7; 79 -4.7; 87 -4.9; 96 -5.1; 106 -5.5; 116 -5.8; 128 -6.2; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.2; 206 -6.0; 227 -5.7; 249 -5.2; 274 -4.7; 302 -4.2; 332 -3.7; 365 -3.2; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.2; 588 -0.7; 647 -0.3; 712 0.2; 783 0.5; 861 0.6; 947 0.3; 1042 -0.3; 1146 -1.2; 1261 -2.1; 1387 -2.6; 1526 -3.2; 1678 -3.8; 1846 -4.3; 2031 -4.3; 2234 -3.6; 2457 -2.9; 2703 -3.0; 2973 -2.5; 3270 -0.7; 3597 0.9; 3957 1.6; 4353 2.0; 4788 2.9; 5267 3.6; 5793 4.0; 6373 2.9; 7010 1.1; 7711 -2.0; 8482 -3.6; 9330 -5.3; 10263 -7.5; 11289 -6.5; 12418 -1.6; 13660 0.0; 15026 0.0; 16529 -2.1; 18182 -5.9; 20000 -1.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats TrueFree GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats TrueFree ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.82 | -8.1 dB |
| Peaking | 28 Hz    | 0.61 | -4.4 dB |
| Peaking | 170 Hz   | 0.59 | -6.1 dB |
| Peaking | 10411 Hz | 3.36 | -8.5 dB |
| Peaking | 18432 Hz | 1.81 | -6.7 dB |
| Peaking | 853 Hz   | 1.55 | 2.6 dB  |
| Peaking | 2018 Hz  | 0.86 | -5.0 dB |
| Peaking | 5824 Hz  | 1.04 | 6.4 dB  |
| Peaking | 8144 Hz  | 1.87 | -4.8 dB |
| Peaking | 14311 Hz | 2.98 | 1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20TrueFree/SoundPeats%20TrueFree.png)