# SoundPeats Q8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.4; 28 -8.7; 31 -8.9; 34 -9.1; 37 -9.3; 41 -9.4; 45 -9.4; 49 -9.5; 54 -9.5; 60 -9.4; 66 -9.2; 72 -9.0; 79 -8.7; 87 -8.5; 96 -8.3; 106 -8.2; 116 -8.0; 128 -7.6; 141 -7.3; 155 -7.3; 170 -7.0; 187 -6.5; 206 -6.1; 227 -5.5; 249 -4.8; 274 -4.1; 302 -3.2; 332 -2.4; 365 -1.5; 402 -0.7; 442 -0.2; 486 0.4; 535 1.1; 588 1.6; 647 1.9; 712 1.7; 783 1.0; 861 0.3; 947 -0.2; 1042 -0.3; 1146 -0.1; 1261 -0.1; 1387 -0.5; 1526 -0.6; 1678 0.0; 1846 0.8; 2031 1.2; 2234 0.9; 2457 -0.5; 2703 -2.2; 2973 -3.8; 3270 -2.9; 3597 -0.6; 3957 0.5; 4353 1.1; 4788 2.0; 5267 2.3; 5793 2.4; 6373 1.3; 7010 -3.2; 7711 -9.1; 8482 -7.5; 9330 -0.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -5.0; 15026 -10.3; 16529 -10.5; 18182 -8.5; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.38 | -9.7 dB  |
| Peaking | 170 Hz   | 1.19 | -3.9 dB  |
| Peaking | 3014 Hz  | 6.47 | -4.2 dB  |
| Peaking | 15401 Hz | 3.35 | -6.5 dB  |
| Peaking | 17899 Hz | 1.03 | -8.5 dB  |
| Peaking | 617 Hz   | 2.4  | 2.7 dB   |
| Peaking | 5987 Hz  | 2.04 | 4.8 dB   |
| Peaking | 7938 Hz  | 3.21 | -13.0 dB |
| Peaking | 10804 Hz | 1.21 | 4.2 dB   |
| Peaking | 13835 Hz | 2.29 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SoundPeats%20Q8/SoundPeats%20Q8.png)