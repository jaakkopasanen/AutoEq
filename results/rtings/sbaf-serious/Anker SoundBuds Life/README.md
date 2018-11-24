# Anker SoundBuds Life

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -6.2; 23 -6.6; 25 -6.9; 28 -7.3; 31 -7.5; 34 -7.5; 37 -7.4; 41 -7.1; 45 -6.8; 49 -6.5; 54 -6.3; 60 -6.2; 66 -6.1; 72 -6.0; 79 -5.8; 87 -5.9; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.8; 141 -7.0; 155 -7.1; 170 -7.3; 187 -7.5; 206 -6.7; 227 -5.4; 249 -3.8; 274 -2.2; 302 -1.4; 332 -1.4; 365 -1.6; 402 -1.6; 442 -1.3; 486 -0.8; 535 -0.1; 588 0.5; 647 1.0; 712 1.3; 783 1.2; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.5; 1526 -3.3; 1678 -4.0; 1846 -4.4; 2031 -4.5; 2234 -4.2; 2457 -4.2; 2703 -4.9; 2973 -5.9; 3270 -5.8; 3597 -5.1; 3957 -6.0; 4353 -8.2; 4788 -9.4; 5267 -9.9; 5793 -6.6; 6373 -2.9; 7010 -0.9; 7711 -2.1; 8482 -2.4; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.32 | -7.1 dB |
| Peaking | 171 Hz  | 1.44 | -5.7 dB |
| Peaking | 1802 Hz | 2.48 | -3.7 dB |
| Peaking | 3017 Hz | 1.98 | -4.3 dB |
| Peaking | 4988 Hz | 2.62 | -9.6 dB |
| Peaking | 302 Hz  | 3.64 | 2.2 dB  |
| Peaking | 302 Hz  | 1.35 | -0.9 dB |
| Peaking | 732 Hz  | 1.6  | 3.0 dB  |
| Peaking | 2299 Hz | 0.2  | -1.7 dB |
| Peaking | 4001 Hz | 0.3  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)