# HiSoundAudio Golden Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 -7.8; 23 -7.8; 25 -7.8; 28 -7.7; 31 -7.6; 34 -7.5; 37 -7.4; 41 -7.3; 45 -7.3; 49 -7.2; 54 -7.1; 60 -7.1; 66 -7.1; 72 -7.1; 79 -7.1; 87 -7.1; 96 -7.2; 106 -7.0; 116 -6.8; 128 -6.7; 141 -6.5; 155 -6.2; 170 -5.9; 187 -5.5; 206 -5.2; 227 -4.7; 249 -4.3; 274 -3.8; 302 -3.3; 332 -2.9; 365 -2.3; 402 -1.9; 442 -1.3; 486 -1.0; 535 -0.5; 588 0.1; 647 0.4; 712 0.4; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -1.7; 1526 -2.2; 1678 -3.1; 1846 -3.6; 2031 -3.5; 2234 -0.8; 2457 2.7; 2703 1.4; 2973 0.8; 3270 1.7; 3597 2.5; 3957 2.4; 4353 1.0; 4788 0.4; 5267 0.5; 5793 -0.9; 6373 -5.4; 7010 -8.4; 7711 -6.4; 8482 -3.4; 9330 -2.8; 10263 -4.7; 11289 -3.2; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.8; 18182 -3.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Golden Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Golden Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.19 | -7.5 dB |
| Peaking | 164 Hz   |  0.78 | -3.3 dB |
| Peaking | 1798 Hz  |  4.65 | -4.1 dB |
| Peaking | 7250 Hz  |  3.6  | -8.7 dB |
| Peaking | 17695 Hz |  2.63 | -4.6 dB |
| Peaking | 737 Hz   |  3.05 | 1.4 dB  |
| Peaking | 2501 Hz  | 10.1  | 3.1 dB  |
| Peaking | 3793 Hz  |  2.85 | 3.1 dB  |
| Peaking | 10641 Hz |  3.65 | -6.1 dB |
| Peaking | 11792 Hz |  1.6  | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Golden%20Crystal/HiSoundAudio%20Golden%20Crystal.png)