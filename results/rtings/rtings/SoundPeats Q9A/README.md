# SoundPeats Q9A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.5; 28 -5.5; 31 -5.5; 34 -5.5; 37 -5.5; 41 -5.6; 45 -5.6; 49 -5.6; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.6; 141 -10.1; 155 -10.3; 170 -10.4; 187 -10.3; 206 -10.1; 227 -9.8; 249 -9.3; 274 -8.7; 302 -8.0; 332 -7.4; 365 -6.6; 402 -5.9; 442 -5.1; 486 -4.2; 535 -3.2; 588 -2.2; 647 -1.3; 712 -0.7; 783 -0.4; 861 -0.1; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.4; 1526 -4.1; 1678 -5.9; 1846 -7.1; 2031 -7.0; 2234 -4.9; 2457 -2.1; 2703 0.6; 2973 2.3; 3270 2.9; 3597 2.9; 3957 2.1; 4353 0.7; 4788 -0.6; 5267 -1.7; 5793 -1.5; 6373 -1.1; 7010 -0.4; 7711 -1.6; 8482 -2.5; 9330 -0.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.08 | -4.7 dB  |
| Peaking | 212 Hz  | 0.53 | -7.1 dB  |
| Peaking | 1959 Hz | 1.32 | -15.8 dB |
| Peaking | 3280 Hz | 0.43 | 19.0 dB  |
| Peaking | 5121 Hz | 0.53 | -13.8 dB |
| Peaking | 17 Hz   | 1.44 | -0.5 dB  |
| Peaking | 822 Hz  | 3.06 | 0.3 dB   |
| Peaking | 1555 Hz | 5.51 | -0.6 dB  |
| Peaking | 6959 Hz | 6.05 | 1.4 dB   |
| Peaking | 8363 Hz | 7.07 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SoundPeats%20Q9A/SoundPeats%20Q9A.png)