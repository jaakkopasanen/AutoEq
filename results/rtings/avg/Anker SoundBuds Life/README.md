# Anker SoundBuds Life

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.4; 31 -7.5; 34 -7.4; 37 -7.3; 41 -6.9; 45 -6.6; 49 -6.2; 54 -6.0; 60 -5.9; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.7; 116 -7.1; 128 -7.3; 141 -7.5; 155 -7.7; 170 -7.9; 187 -8.1; 206 -7.2; 227 -5.8; 249 -4.4; 274 -2.9; 302 -2.2; 332 -2.3; 365 -2.6; 402 -2.7; 442 -2.4; 486 -2.0; 535 -1.3; 588 -0.6; 647 -0.0; 712 0.4; 783 0.7; 861 0.9; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.4; 1526 -2.9; 1678 -3.7; 1846 -4.5; 2031 -4.9; 2234 -4.7; 2457 -4.7; 2703 -5.7; 2973 -7.5; 3270 -8.4; 3597 -8.3; 3957 -8.4; 4353 -9.5; 4788 -11.0; 5267 -12.8; 5793 -10.5; 6373 -6.6; 7010 -4.1; 7711 -3.6; 8482 -1.9; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -4.1; 16529 -4.5; 18182 -5.1; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.51 | -7.0 dB |
| Peaking | 138 Hz  | 0.79 | -5.7 dB |
| Peaking | 195 Hz  | 2.73 | -3.0 dB |
| Peaking | 3317 Hz | 0.89 | -7.0 dB |
| Peaking | 5330 Hz | 2.89 | -9.4 dB |
| Peaking | 440 Hz  | 3.42 | -1.5 dB |
| Peaking | 839 Hz  | 1.89 | 2.3 dB  |
| Peaking | 1963 Hz | 1.03 | -1.7 dB |
| Peaking | 2499 Hz | 3.51 | 2.4 dB  |
| Peaking | 9558 Hz | 4.69 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)