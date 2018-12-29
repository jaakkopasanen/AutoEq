# SoundPeats Q8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -8.1; 23 -8.4; 25 -8.6; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.2; 45 -9.1; 49 -9.1; 54 -9.1; 60 -9.1; 66 -9.1; 72 -9.0; 79 -8.8; 87 -8.8; 96 -8.7; 106 -8.7; 116 -8.5; 128 -8.2; 141 -7.8; 155 -7.9; 170 -7.7; 187 -7.1; 206 -6.6; 227 -6.0; 249 -5.4; 274 -4.8; 302 -4.1; 332 -3.3; 365 -2.5; 402 -1.8; 442 -1.3; 486 -0.8; 535 -0.1; 588 0.5; 647 0.8; 712 0.9; 783 0.5; 861 0.1; 947 -0.2; 1042 -0.3; 1146 -0.3; 1261 -0.4; 1387 -0.5; 1526 -0.2; 1678 0.4; 1846 0.8; 2031 0.8; 2234 0.5; 2457 -0.9; 2703 -3.0; 2973 -5.4; 3270 -5.5; 3597 -3.7; 3957 -2.0; 4353 -0.3; 4788 0.4; 5267 -0.6; 5793 -1.5; 6373 -2.5; 7010 -6.6; 7711 -11.6; 8482 -8.5; 9330 -0.8; 10263 0.0; 11289 -0.2; 12418 -5.8; 13660 -12.1; 15026 -16.2; 16529 -16.9; 18182 -16.1; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.3  | -9.2 dB  |
| Peaking | 171 Hz   | 0.94 | -4.1 dB  |
| Peaking | 3156 Hz  | 4.24 | -5.9 dB  |
| Peaking | 16159 Hz | 1.05 | -15.7 dB |
| Peaking | 19336 Hz | 1.43 | -8.7 dB  |
| Peaking | 648 Hz   | 2.77 | 1.8 dB   |
| Peaking | 2014 Hz  | 4.56 | 1.6 dB   |
| Peaking | 4884 Hz  | 4.22 | 2.0 dB   |
| Peaking | 7853 Hz  | 4.21 | -11.5 dB |
| Peaking | 10435 Hz | 2.83 | 7.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q8/SoundPeats%20Q8.png)