# SoundPeats Q9A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.5; 28 -5.5; 31 -5.5; 34 -5.5; 37 -5.5; 41 -5.6; 45 -5.6; 49 -5.6; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.6; 141 -10.1; 155 -10.3; 170 -10.4; 187 -10.3; 206 -10.1; 227 -9.8; 249 -9.3; 274 -8.7; 302 -8.0; 332 -7.4; 365 -6.6; 402 -5.9; 442 -5.1; 486 -4.2; 535 -3.2; 588 -2.2; 647 -1.3; 712 -0.7; 783 -0.4; 861 -0.1; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.4; 1526 -4.1; 1678 -5.9; 1846 -7.1; 2031 -7.0; 2234 -4.8; 2457 -2.1; 2703 0.4; 2973 1.8; 3270 2.2; 3597 1.9; 3957 0.9; 4353 -0.6; 4788 -2.4; 5267 -4.3; 5793 -4.0; 6373 -2.3; 7010 -1.3; 7711 -3.0; 8482 -3.2; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.13 | -5.1 dB |
| Peaking | 201 Hz   | 0.69 | -7.8 dB |
| Peaking | 1881 Hz  | 3.6  | -7.9 dB |
| Peaking | 5636 Hz  | 3.81 | -4.6 dB |
| Peaking | 22293 Hz | 2.2  | -1.0 dB |
| Peaking | 856 Hz   | 1.13 | 4.7 dB  |
| Peaking | 899 Hz   | 0.58 | -3.0 dB |
| Peaking | 2249 Hz  | 7.68 | -1.9 dB |
| Peaking | 3193 Hz  | 2.53 | 3.7 dB  |
| Peaking | 8221 Hz  | 6.58 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q9A/SoundPeats%20Q9A.png)