# Sennheiser AMBEO Smart Headset

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 1.6; 28 0.7; 31 0.1; 34 -0.4; 37 -0.7; 41 -1.1; 45 -1.4; 49 -1.6; 54 -2.0; 60 -2.6; 66 -3.1; 72 -3.6; 79 -4.1; 87 -4.7; 96 -5.3; 106 -5.9; 116 -6.5; 128 -7.0; 141 -7.4; 155 -7.6; 170 -7.6; 187 -7.5; 206 -7.5; 227 -7.4; 249 -7.1; 274 -6.7; 302 -6.2; 332 -5.6; 365 -5.0; 402 -4.4; 442 -3.7; 486 -3.1; 535 -2.3; 588 -1.5; 647 -0.7; 712 0.1; 783 0.7; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -1.7; 1526 -1.7; 1678 -1.6; 1846 -1.4; 2031 -1.0; 2234 0.2; 2457 1.7; 2703 2.5; 2973 2.5; 3270 2.1; 3597 1.4; 3957 0.6; 4353 -0.3; 4788 -0.6; 5267 -1.4; 5793 -3.2; 6373 -6.6; 7010 -5.9; 7711 -3.7; 8482 -6.0; 9330 -10.5; 10263 -11.0; 11289 -8.4; 12418 -7.3; 13660 -4.6; 15026 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser AMBEO Smart Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser AMBEO Smart Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.88 | 4.2 dB   |
| Peaking | 175 Hz   | 0.55 | -8.0 dB  |
| Peaking | 3033 Hz  | 2.81 | 3.3 dB   |
| Peaking | 6498 Hz  | 5.95 | -5.1 dB  |
| Peaking | 10291 Hz | 1.8  | -11.4 dB |
| Peaking | 370 Hz   | 1.92 | -0.8 dB  |
| Peaking | 802 Hz   | 2.04 | 2.4 dB   |
| Peaking | 1493 Hz  | 2.02 | -1.9 dB  |
| Peaking | 13084 Hz | 3.82 | -4.5 dB  |
| Peaking | 14486 Hz | 1.45 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20AMBEO%20Smart%20Headset/Sennheiser%20AMBEO%20Smart%20Headset.png)