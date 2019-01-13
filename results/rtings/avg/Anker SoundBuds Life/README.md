# Anker SoundBuds Life
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.4; 31 -7.5; 34 -7.4; 37 -7.3; 41 -6.9; 45 -6.6; 49 -6.2; 54 -6.0; 60 -5.9; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.7; 116 -7.1; 128 -7.3; 141 -7.5; 155 -7.7; 170 -7.9; 187 -8.1; 206 -7.2; 227 -5.8; 249 -4.4; 274 -2.9; 302 -2.2; 332 -2.3; 365 -2.6; 402 -2.7; 442 -2.4; 486 -2.0; 535 -1.3; 588 -0.6; 647 -0.0; 712 0.4; 783 0.7; 861 0.9; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.4; 1526 -2.9; 1678 -3.7; 1846 -4.5; 2031 -4.9; 2234 -4.7; 2457 -4.7; 2703 -5.7; 2973 -7.5; 3270 -8.4; 3597 -8.3; 3957 -8.4; 4353 -9.5; 4788 -11.0; 5267 -12.9; 5793 -10.5; 6373 -6.6; 7010 -4.3; 7711 -4.6; 8482 -3.5; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -4.1; 16529 -4.5; 18182 -5.1; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.51 | -7.0 dB  |
| Peaking | 138 Hz   | 0.8  | -5.7 dB  |
| Peaking | 194 Hz   | 2.67 | -3.1 dB  |
| Peaking | 3412 Hz  | 0.82 | -6.9 dB  |
| Peaking | 5341 Hz  | 2.77 | -8.7 dB  |
| Peaking | 436 Hz   | 3.42 | -1.5 dB  |
| Peaking | 825 Hz   | 2.22 | 2.1 dB   |
| Peaking | 1675 Hz  | 2.82 | -1.1 dB  |
| Peaking | 11628 Hz | 1.71 | 2.9 dB   |
| Peaking | 20855 Hz | 0.56 | -10.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)