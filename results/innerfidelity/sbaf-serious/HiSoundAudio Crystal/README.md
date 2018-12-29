# HiSoundAudio Crystal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.3; 25 -1.4; 28 -1.6; 31 -1.7; 34 -1.8; 37 -1.9; 41 -2.1; 45 -2.2; 49 -2.3; 54 -2.6; 60 -2.8; 66 -3.2; 72 -3.4; 79 -3.7; 87 -4.1; 96 -4.3; 106 -4.6; 116 -4.6; 128 -4.8; 141 -4.9; 155 -5.0; 170 -5.0; 187 -4.9; 206 -4.7; 227 -4.4; 249 -4.2; 274 -3.8; 302 -3.5; 332 -3.1; 365 -2.7; 402 -2.2; 442 -1.6; 486 -1.3; 535 -0.8; 588 -0.1; 647 0.2; 712 0.3; 783 0.7; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.7; 1261 -1.6; 1387 -2.6; 1526 -3.8; 1678 -4.5; 1846 -4.6; 2031 -3.6; 2234 -1.9; 2457 -0.0; 2703 6.0; 2973 2.8; 3270 -0.6; 3597 0.5; 3957 1.8; 4353 -0.3; 4788 -1.2; 5267 -1.5; 5793 -3.5; 6373 -6.8; 7010 -4.6; 7711 -0.8; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.7; 13660 -1.5; 15026 -2.1; 16529 -3.2; 18182 -0.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 102 Hz   |  0.54 | -3.9 dB |
| Peaking | 226 Hz   |  1.09 | -2.7 dB |
| Peaking | 1788 Hz  |  2.45 | -5.2 dB |
| Peaking | 2730 Hz  |  7.05 | 7.6 dB  |
| Peaking | 6426 Hz  |  4.79 | -7.2 dB |
| Peaking | 25 Hz    |  1.5  | -0.7 dB |
| Peaking | 780 Hz   |  2.83 | 1.5 dB  |
| Peaking | 3953 Hz  | 10.61 | 2.2 dB  |
| Peaking | 8489 Hz  |  4.88 | 1.0 dB  |
| Peaking | 16190 Hz |  2.01 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Crystal/HiSoundAudio%20Crystal.png)