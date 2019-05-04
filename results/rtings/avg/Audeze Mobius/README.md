# Audeze Mobius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.2; 25 -7.0; 28 -6.7; 31 -6.6; 34 -6.6; 37 -6.7; 41 -6.7; 45 -6.6; 49 -6.3; 54 -6.0; 60 -5.8; 66 -5.7; 72 -5.6; 79 -5.6; 87 -5.6; 96 -5.7; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.6; 170 -6.7; 187 -6.8; 206 -6.8; 227 -6.7; 249 -6.7; 274 -6.5; 302 -6.2; 332 -5.9; 365 -5.6; 402 -5.1; 442 -4.9; 486 -5.5; 535 -6.1; 588 -6.4; 647 -6.2; 712 -6.1; 783 -6.3; 861 -6.2; 947 -5.8; 1042 -5.7; 1146 -6.1; 1261 -6.3; 1387 -6.2; 1526 -6.5; 1678 -7.3; 1846 -8.0; 2031 -8.0; 2234 -7.7; 2457 -7.7; 2703 -7.9; 2973 -8.0; 3270 -8.1; 3597 -6.1; 3957 -1.0; 4353 -0.8; 4788 -1.6; 5267 -1.8; 5793 -1.1; 6373 -0.5; 7010 -3.3; 7711 -7.3; 8482 -9.2; 9330 -7.0; 10263 -6.3; 11289 -7.0; 12418 -5.8; 13660 -5.8; 15026 -10.0; 16529 -14.4; 18182 -15.6; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Mobius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Mobius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 3489 Hz  | 0.73 | -10.3 dB |
| Peaking | 4099 Hz  | 4.84 | 6.5 dB   |
| Peaking | 6685 Hz  | 0.59 | 17.0 dB  |
| Peaking | 8211 Hz  | 1.68 | -13.5 dB |
| Peaking | 18468 Hz | 0.5  | -11.8 dB |
| Peaking | 21 Hz    | 1.1  | -1.7 dB  |
| Peaking | 207 Hz   | 1.57 | -1.0 dB  |
| Peaking | 422 Hz   | 4.97 | 1.2 dB   |
| Peaking | 11136 Hz | 6.97 | -1.8 dB  |
| Peaking | 13813 Hz | 6.19 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20Mobius/Audeze%20Mobius.png)